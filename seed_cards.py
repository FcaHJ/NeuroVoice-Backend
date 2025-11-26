from app import create_app, db
from models.card import Card

app = create_app()

cards_data = [
    { "id": 1, "image": "assets/image/jugar.png", "description": "Jugar", "category": "Deporte", "fav": True },
    { "id": 2, "image": "assets/image/comida.png", "description": "Comida", "category": "Necesidades", "fav": False },
    { "id": 3, "image": "assets/image/fuera.png", "description": "Fuera", "category": "Ocio", "fav": False },
    { "id": 4, "image": "assets/image/cine.png", "description": "Cine", "category": "Ocio", "fav": False },
    { "id": 5, "image": "assets/image/cantar.png", "description": "Cantar", "category": "Ocio", "fav": False },
    { "id": 6, "image": "assets/image/barrer.png", "description": "Barrer", "category": "Hogar", "fav": False },
    { "id": 7, "image": "assets/image/cocinar.png", "description": "Cocinar", "category": "Hogar", "fav": False },
    { "id": 8, "image": "assets/image/voleibol.png", "description": "Voleibol", "category": "Deporte", "fav": False },
    { "id": 9, "image": "assets/image/tenis.png", "description": "Tenis", "category": "Deporte", "fav": False },
    { "id": 10, "image": "assets/image/nadar.png", "description": "Nadar", "category": "Deporte", "fav": False },
    { "id": 11, "image": "assets/image/futbol.png", "description": "Fútbol", "category": "Deporte", "fav": False },
    { "id": 12, "image": "assets/image/basquetbol.png", "description": "Basquetbol", "category": "Deporte", "fav": False },
    { "id": 13, "image": "assets/image/adios.png", "description": "Adios", "category": "Emociones", "fav": False },
    { "id": 14, "image": "assets/image/agua.png", "description": "Agua", "category": "Alimentación", "fav": False },
    { "id": 15, "image": "assets/image/jugo.png", "description": "Jugo", "category": "Alimentación", "fav": False },
    { "id": 16, "image": "assets/image/carne.png", "description": "Carne", "category": "Alimentación", "fav": False },
    { "id": 17, "image": "assets/image/bailar.png", "description": "Bailar", "category": "Deporte", "fav": False },
    { "id": 18, "image": "assets/image/cansancio.png", "description": "Cansancio", "category": "Necesidades", "fav": False },
    { "id": 19, "image": "assets/image/calor.png", "description": "Calor", "category": "Necesidades", "fav": False },
    { "id": 20, "image": "assets/image/frio.png", "description": "Frio", "category": "Necesidades", "fav": False },
    { "id": 21, "image": "assets/image/hola.png", "description": "Hola", "category": "Emociones", "fav": False },
    { "id": 22, "image": "assets/image/correr.png", "description": "Correr", "category": "Deporte", "fav": False },
    { "id": 23, "image": "assets/image/enojo.png", "description": "Enojo", "category": "Emociones", "fav": False },
    { "id": 24, "image": "assets/image/feliz.png", "description": "Feliz", "category": "Emociones", "fav": False },
    { "id": 25, "image": "assets/image/enfermo.png", "description": "Enfermo", "category": "Necesidades", "fav": False },
    { "id": 26, "image": "assets/image/dormir.png", "description": "Dormir", "category": "Necesidades", "fav": False },
    { "id": 27, "image": "assets/image/estudiar.png", "description": "Estudiar", "category": "Necesidades", "fav": False },
    { "id": 28, "image": "assets/image/jugar-videojuegos.png", "description": "Videojuegos", "category": "Ocio", "fav": False },
    { "id": 29, "image": "assets/image/leer.png", "description": "Leer", "category": "Ocio", "fav": False },
    { "id": 30, "image": "assets/image/limpiar.png", "description": "Limpiar", "category": "Hogar", "fav": False },
    { "id": 31, "image": "assets/image/pintar.png", "description": "Pintar", "category": "Ocio", "fav": False },
    { "id": 32, "image": "assets/image/redes-sociales.png", "description": "Redes sociales", "category": "Tecnología", "fav": False },
    { "id": 33, "image": "assets/image/celular.png", "description": "Celular", "category": "Tecnología", "fav": False },
    { "id": 34, "image": "assets/image/tablet.png", "description": "Tablet", "category": "Tecnología", "fav": False },
    { "id": 35, "image": "assets/image/computador.png", "description": "Computador", "category": "Tecnología", "fav": False },
    { "id": 36, "image": "assets/image/tomar-fotos.png", "description": "Tomar fotos", "category": "Ocio", "fav": False },
    { "id": 37, "image": "assets/image/postre.png", "description": "Postre", "category": "Alimentacion", "fav": False },
    { "id": 38, "image": "assets/image/ver-television.png", "description": "Ver televisión", "category": "Ocio", "fav": False },
    { "id": 39, "image": "assets/image/silencio.png", "description": "Silencio", "category": "Emociones", "fav": False },
    { "id": 40, "image": "assets/image/lavar-platos.png", "description": "Lavar platos", "category": "Hogar", "fav": False },
    { "id": 41, "image": "assets/image/escuchar-musica.png", "description": "Musica", "category": "Ocio", "fav": False },
    { "id": 42, "image": "assets/image/desagrado.png", "description": "Desagrado", "category": "Emociones", "fav": False },
    { "id": 43, "image": "assets/image/confusion.png", "description": "Confusión", "category": "Emociones", "fav": False },
    { "id": 44, "image": "assets/image/casa.png", "description": "Casa", "category": "Hogar", "fav": False },
    { "id": 45, "image": "assets/image/triste.png", "description": "Triste", "category": "Emociones", "fav": False },
    { "id": 46, "image": "assets/image/familia.png", "description": "Familia", "category": "Relaciones", "fav": False },
    { "id": 47, "image": "assets/image/amigos.png", "description": "Amigos", "category": "Relaciones", "fav": False },
    { "id": 48, "image": "assets/image/perro.png", "description": "Perro", "category": "Animales", "fav": False },
    { "id": 49, "image": "assets/image/gato.png", "description": "Gato", "category": "Animales", "fav": False },
    { "id": 50, "image": "assets/image/conejo.png", "description": "Conejo", "category": "Animales", "fav": False }
]

with app.app_context():
    if Card.query.count() == 0:
        for c in cards_data:
            card = Card(
                id=c["id"],
                image=c["image"],
                description=c["description"],
                category=c["category"],
                fav=c["fav"]
            )
            db.session.add(card)

        db.session.commit()
        print("✔ Cartas insertadas correctamente")
    else:
        print("✔ Cartas ya existen, no se insertaron")
