from flask import Flask
from flask_cors import CORS
from models import db

def create_app():
    app = Flask(__name__)
    CORS(app)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///neurovoice.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    # Importar modelos DESPUÉS de init_app
    with app.app_context():
        from models.card import Card
        from models.collection import Collection
        from models.user import User
        db.create_all()

    # Importar rutas (sin importar los modelos dentro de las rutas)
    from routes.card_routes import card_routes
    from routes.collection_routes import collection_routes
    from routes.user_routes import user_routes

    app.register_blueprint(card_routes, url_prefix="/api/cards")
    app.register_blueprint(collection_routes, url_prefix="/api/collections")
    app.register_blueprint(user_routes, url_prefix="/api/users")

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=5000, debug=True)
