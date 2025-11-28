from flask import Blueprint, request, jsonify
from models import db
from models.user import User
from flask_cors import cross_origin
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
import datetime

SECRET_KEY = "cambia_esto_por_algo_muy_secreto"

user_routes = Blueprint("user_routes", __name__)

@user_routes.get("/")
@cross_origin()
def get_users():
    users = User.query.all()
    return jsonify([u.to_dict() for u in users])

@user_routes.post("/register")
@cross_origin()
def register():
    data = request.json

    # Validaciones básicas
    if not data.get("username") or not data.get("password"):
        return jsonify({"error": "Username y password son requeridos"}), 400

    # Verificar si ya existe
    if User.query.filter_by(username=data["username"]).first():
        return jsonify({"error": "El usuario ya existe"}), 400

    # Hashear contraseña
    hashed_pw = generate_password_hash(data["password"])

    user = User(
        username=data["username"],
        password=hashed_pw
    )

    db.session.add(user)
    db.session.commit()

    return jsonify(user.to_dict()), 201

@user_routes.post("/login")
@cross_origin()
def login():
    data = request.json

    user = User.query.filter_by(username=data["username"]).first()

    # Validar existencia + contraseña
    if not user or not check_password_hash(user.password, data["password"]):
        return jsonify({"error": "Credenciales inválidas"}), 401

    # Generar token JWT
    token = jwt.encode({
        "user_id": user.id,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=12)
    }, SECRET_KEY, algorithm="HS256")

    return jsonify({
        "user": user.to_dict(),
        "token": token
    })
