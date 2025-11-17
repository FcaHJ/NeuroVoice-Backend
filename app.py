from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Importar rutas
from routes.card_routes import card_routes

def create_app():
    app = Flask(__name__)
    CORS(app)

    # Configurar SQLite
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///neurovoice.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Inicializar DB
    db.init_app(app)

    # Registrar rutas
    app.register_blueprint(card_routes, url_prefix="/api/cards")

    # Crear tablas si no existen
    with app.app_context():
        db.create_all()

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
