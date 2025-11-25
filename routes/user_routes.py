from flask import Blueprint, request, jsonify
from app import db
from models.user import User

user_routes = Blueprint("user_routes", __name__)

@user_routes.get("/")
def get_users():
    users = User.query.all()
    return jsonify([u.to_dict() for u in users])

@user_routes.post("/register")
def register():
    data = request.json
    user = User(**data)
    db.session.add(user)
    db.session.commit()
    return jsonify(user.to_dict()), 201

@user_routes.post("/login")
def login():
    data = request.json
    user = User.query.filter_by(
        username=data["username"],
        password=data["password"]
    ).first()
    
    if not user:
        return jsonify({"error": "Invalid credentials"}), 401

    return jsonify(user.to_dict())
