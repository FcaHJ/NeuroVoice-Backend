from flask import Blueprint, request, jsonify
from models import db
from models.user import User
from flask_cors import cross_origin


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
    user = User(**data)
    db.session.add(user)
    db.session.commit()
    return jsonify(user.to_dict()), 201

@user_routes.post("/login")
@cross_origin()
def login():
    data = request.json
    user = User.query.filter_by(
        username=data["username"],
        password=data["password"]
    ).first()
    
    if not user:
        return jsonify({"error": "Invalid credentials"}), 401

    return jsonify(user.to_dict())
