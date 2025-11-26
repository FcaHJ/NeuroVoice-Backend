from . import db

class Card(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    image = db.Column(db.String(500), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    category = db.Column(db.String(200), nullable=False)
    fav = db.Column(db.Boolean, default=False)
    collection_id = db.Column(db.Integer, db.ForeignKey('collection.id'))

    def to_dict(self):
        return {
            "id": self.id,
            "image": self.image,
            "description": self.description,
            "category": self.category,
            "fav": self.fav,
            "collection_id": self.collection_id
        }



