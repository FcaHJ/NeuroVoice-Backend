from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    CORS(app)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///neurovoice.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    # Importar modelos
    from models.card import Card
    from models.collection import Collection
    from models.user import User

    # Importar rutas
    from routes.card_routes import card_routes
    from routes.collection_routes import collection_routes
    from routes.user_routes import user_routes

    # Registrar rutas
    app.register_blueprint(card_routes, url_prefix="/api/cards")
    app.register_blueprint(collection_routes, url_prefix="/api/collections")
    app.register_blueprint(user_routes, url_prefix="/api/users")

    # Crear tablas
    with app.app_context():
        db.create_all()

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=5000, debug=True)
