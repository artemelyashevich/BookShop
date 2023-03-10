from flask import Response
from werkzeug.security import check_password_hash

from backend.config import ALLOWED_EXTENSIONS
from backend.model.User import User


class UserRepository:
    def __init__(self, db):
        self.db = db
        self.users = self.db.session.query(User).all()

    def get_all_users(self):
        data = []
        for user in self.users:
            data.append({
                "name": user.name,
                "surname": user.surname,
                "email": user.email,
            })
        return data

    def create(self, data):
        try:
            user = User(data["name"], data["surname"], data["email"], data["password"])
            self.db.session.add(user)
            self.db.session.commit()
            return Response(200)
        except Exception as e:
            print(e)
            return Response(500)

    def update(self, id, data):
        if self.check_data(data):
            return Response(status=400)
        try:

            user = self.search_user(id)
            user.name = data["name"]
            user.surname = data["surname"]
            user.email = data["email"]
            user.img = data["img"]

            if check_password_hash(user.password, data["password"]):
                self.db.session.commit()
                return Response(status=200)
            return Response(status=400)
        except Exception as e:
            print(e)
            return Response(status=500)

    def delete(self, id):
        if id == "":
            return Response(status=400)
        try:
            if id.isdigit():
                self.db.session.delete(self.search_user(id))
                self.db.session.commit()
                return Response(status=200)
        except Exception as e:
            print(e)
            return Response(status=500)

    def search_user(self, _id):
        return self.db.session.query(User).filter_by(id=_id).first()

    def set_img(self, id, data):
        user = self.search_user(id)
        user.img = data
        self.db.session.commit()
        return Response(status=200)

    @staticmethod
    def allowed_file(filename):
        return '.' in filename and \
               filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

    @staticmethod
    def check_data(data):
        if (data["name"] == '') or (data["surname"] == '') \
                or (data["password"] == '') or (data["email"] == ''):
            return True
        elif (data["name"] is None) or (data["surname"] is None) \
                or (data["password"] is None) or (data["email"] is None):
            return True
