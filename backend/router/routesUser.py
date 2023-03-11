import os
from __main__ import app

from flask import jsonify, request, Response

from backend.action.UserRepository import UserRepository
from backend.database.cfg import db

userRepository = UserRepository(db)


@app.route("/user", methods=["POST"])
def create_user():
    return userRepository.create(request.get_json())


@app.route("/users")
def get_users():
    return userRepository.get_all_users()


@app.route("/user/<id>", methods=["PUT"])
def update_user(id):
    return userRepository.update(id, request.get_json())


@app.route("/user/<id>", methods=["DELETE"])
def delete_user(id):
    return userRepository.delete(id)


@app.route("/user/img/upload/<id>", methods=["POST"])
def upload_img():
    file = request.files["file"]
    print(file)
    if file and userRepository.allowed_file(file.filename):
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
        userRepository.set_img(id=id, data=file.name)
    return Response(status=200)



@app.errorhandler(500)
def server_error(e):
    return 'Server error'


@app.errorhandler(400)
def bad_request(e):
    return 'Bad request'
