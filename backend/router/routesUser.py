from __main__ import app

from flask import jsonify, request

from backend.action.UserRepository import UserRepository
from backend.database.cfg import db


@app.route("/user", methods=["POST"])
def create_user():
    return UserRepository(db).create(request.get_json())


@app.route("/users")
def get_users():
    return UserRepository(db).get_all_users()


@app.route("/user/<id>", methods=["PUT"])
def update_user(id):
    return UserRepository(db).update(id, request.get_json())
