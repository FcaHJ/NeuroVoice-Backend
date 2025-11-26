from flask import Blueprint, request, jsonify
from models import db
from models.card import Card
from models.collection import Collection
from flask_cors import cross_origin


card_routes = Blueprint("card_routes", __name__)

@card_routes.get("/")
@cross_origin()
def get_cards():
    cards = Card.query.all()
    return jsonify([c.to_dict() for c in cards]), 200

@card_routes.get("/<int:id>")
@cross_origin()
def get_card(id):
    card = Card.query.get(id)
    if not card:
        return jsonify({"error": "Card not found"}), 404
    return jsonify(card.to_dict()), 200

@card_routes.post("/cards")
@cross_origin()
def create_card():
    data = request.json
    card = Card(
        name=data["name"],
        type=data["type"],
        description=data.get("description"),
        collection_id=data.get("collection_id")
    )
    db.session.add(card)
    db.session.commit()
    return jsonify(card.to_dict()), 201

@card_routes.put("/<int:id>")
@cross_origin()
def update_card(id):
    data = request.json or {}
    card = Card.query.get(id)
    if not card:
        return jsonify({"error": "Card not found"}), 404

    card.name = data.get("name", card.name)
    card.description = data.get("description", card.description)
    card.image = data.get("image", card.image)
    # permitir cambiar colección
    card.collection_id = data.get("collection_id", card.collection_id)

    db.session.commit()
    return jsonify(card.to_dict()), 200

@card_routes.delete("/<int:id>")
@cross_origin()
def delete_card(id):
    card = Card.query.get(id)
    if not card:
        return jsonify({"error": "Card not found"}), 404
    db.session.delete(card)
    db.session.commit()
    return jsonify({"message": "Card deleted"}), 200


@card_routes.put("/<int:id>/fav")
@cross_origin()
def toggle_fav(id):
    data = request.json or {}
    card = Card.query.get(id)

    if not card:
        return jsonify({"error": "Card not found"}), 404

    # Actualizar favorito
    card.fav = data.get("fav", card.fav)

    db.session.commit()
    return jsonify(card.to_dict()), 200