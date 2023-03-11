from datetime import datetime
from werkzeug.security import generate_password_hash

from flask import jsonify

from backend.config import default_user
from backend.database.cfg import db


class User(db.Model):
    __tablename__ = 'user'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    surname = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    password = db.Column(db.String)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    img = db.Column(db.String, default=default_user)

    def __init__(self, name, surname, email, password):
        self.name = name
        self.surname = surname
        self.email = email
        self.password = self.hash_password(password)

    def convert_to_json(self):
        return jsonify({
            "id": int(self.id),
            "name": self.name,
            "surname": self.surname,
            "email": self.email,
            "img": self.img,
        })

    @staticmethod
    def hash_password(psw):
        return generate_password_hash(psw)

    def __repr__(self):
        return self.name
