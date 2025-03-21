from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique=True)
    email = db.Column(db.String(30), unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return f'<user {self.username}'

