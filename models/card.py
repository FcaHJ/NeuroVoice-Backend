from app import db

class Card(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200))
    description = db.Column(db.String(500))
    image = db.Column(db.String(500))
    collection_id = db.Column(db.Integer, db.ForeignKey('collection.id'))

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "image": self.image,
            "collection_id": self.collection_id
        }
