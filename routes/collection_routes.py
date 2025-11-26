from flask import Blueprint, request, jsonify
from models import db
from models.collection import Collection
from models.card import Card
from flask_cors import cross_origin


collection_routes = Blueprint("collection_routes", __name__)

@collection_routes.get("/")
@cross_origin()
def get_collections():
    cols = Collection.query.all()
    return jsonify([c.to_dict() for c in cols]), 200

@collection_routes.get("/<int:id>")
@cross_origin()
def get_collection(id):
    col = Collection.query.get(id)
    if not col:
        return jsonify({"error": "Collection not found"}), 404
    return jsonify(col.to_dict()), 200

@collection_routes.post("/")
@cross_origin()
def create_collection():
    data = request.json or {}
    col = Collection(
        name=data.get("name"),
        max_cards=data.get("max_cards", 5)
    )
    db.session.add(col)
    db.session.commit()
    return jsonify(col.to_dict()), 201

@collection_routes.put("/<int:id>")
@cross_origin()
def update_collection(id):
    data = request.json or {}
    col = Collection.query.get(id)
    if not col:
        return jsonify({"error": "Collection not found"}), 404
    col.name = data.get("name", col.name)
    col.max_cards = data.get("max_cards", col.max_cards)
    db.session.commit()
    return jsonify(col.to_dict()), 200

@collection_routes.delete("/<int:id>")
@cross_origin()
def delete_collection(id):
    col = Collection.query.get(id)
    if not col:
        return jsonify({"error": "Collection not found"}), 404
    db.session.delete(col)
    db.session.commit()
    return jsonify({"message": "Collection deleted"}), 200

# Añadir carta a colección (si la carta existe o crearla en el proceso)
@collection_routes.post("/<int:id>/add/<int:card_id>")
@cross_origin()
def add_card_to_collection(id, card_id):
    col = Collection.query.get(id)
    if not col:
        return jsonify({"error": "Collection not found"}), 404

    card = Card.query.get(card_id)
    if not card:
        return jsonify({"error": "Card not found"}), 404

    # Verificar límite
    if col.max_cards and len(col.cards) >= col.max_cards:
        return jsonify({"error": "Collection has reached max_cards"}), 400

    card.collection_id = col.id
    db.session.commit()
    return jsonify(col.to_dict()), 200

# Quitar carta de colección
@collection_routes.delete("/<int:id>/cards/<int:card_id>")
@cross_origin()
def remove_card_from_collection(id, card_id):
    col = Collection.query.get(id)
    if not col:
        return jsonify({"error": "Collection not found"}), 404

    card = Card.query.get(card_id)
    if not card or card.collection_id != col.id:
        return jsonify({"error": "Card not in this collection"}), 404

    card.collection_id = None
    db.session.commit()
    return jsonify({"message": "Card removed from collection"}), 200
