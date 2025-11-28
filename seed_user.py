from app import create_app, db
from models.user import User
from werkzeug.security import generate_password_hash

app = create_app()

users_data = [
    {
        "username": "admin",
        "password": "admin123"
    },
    {
        "username": "esteban",
        "password": "1234"
    }
]

with app.app_context():
    if User.query.count() == 0:
        for u in users_data:
            user = User(
                username=u["username"],
                password=generate_password_hash(u["password"])
            )
            db.session.add(user)

        db.session.commit()
        print("✔ Usuarios insertados correctamente")
    else:
        print("✔ Usuarios ya existen, no se insertaron")
