from flask import Blueprint, request, jsonify
from app import db
from models.card import Card
from models.collection import Collection

card_routes = Blueprint("card_routes", __name__)

@card_routes.get("/")
def get_cards():
    cards = Card.query.all()
    return jsonify([c.to_dict() for c in cards]), 200

@card_routes.get("/<int:id>")
def get_card(id):
    card = Card.query.get(id)
    if not card:
        return jsonify({"error": "Card not found"}), 404
    return jsonify(card.to_dict()), 200

@card_routes.post("/")
def create_card():
    data = request.json or {}
    # permitimos que venga collection_id o no
    card = Card(
        title=data.get("title"),
        description=data.get("description"),
        image=data.get("image"),
        collection_id=data.get("collection_id")
    )
    db.session.add(card)
    db.session.commit()
    return jsonify(card.to_dict()), 201

@card_routes.put("/<int:id>")
def update_card(id):
    data = request.json or {}
    card = Card.query.get(id)
    if not card:
        return jsonify({"error": "Card not found"}), 404

    card.title = data.get("title", card.title)
    card.description = data.get("description", card.description)
    card.image = data.get("image", card.image)
    # permitir cambiar colección
    card.collection_id = data.get("collection_id", card.collection_id)

    db.session.commit()
    return jsonify(card.to_dict()), 200

@card_routes.delete("/<int:id>")
def delete_card(id):
    card = Card.query.get(id)
    if not card:
        return jsonify({"error": "Card not found"}), 404
    db.session.delete(card)
    db.session.commit()
    return jsonify({"message": "Card deleted"}), 200
