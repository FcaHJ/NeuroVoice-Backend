from . import db

class Collection(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), unique=True, nullable=False)
    max_cards = db.Column(db.Integer)
    cards = db.relationship("Card", backref="collection", cascade="all, delete")

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "max_cards": self.max_cards,
            "cards": [c.to_dict() for c in self.cards]
        }
