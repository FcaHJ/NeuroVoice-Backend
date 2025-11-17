from flask import Flask
from flask_cors import CORS

# Importar rutas
from routes.card_routes import card_routes

def create_app():
    app = Flask(__name__)
    CORS(app)

    # Registrar blueprints
    app.register_blueprint(card_routes, url_prefix="/api/cards")

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
