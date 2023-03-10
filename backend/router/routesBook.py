import os

from flask import jsonify, request, Response, redirect, url_for, send_file
from __main__ import app
from backend.database.cfg import db
from backend.action.BookRepository import BookRepository

bookRepository = BookRepository(db)


@app.route("/books")
def get_books():
    first = request.args.get("first")
    last = request.args.get("last")
    if first is None and last is None:
        return bookRepository.get_books(1, bookRepository.count())
    if first is None or last is None:
        return Response(400)
    return bookRepository.get_books(int(first), int(last))


@app.route("/book/<id>")
def get_book(id):
    return bookRepository.search_by_id(id).convert_to_json()


@app.route("/book", methods=["POST"])
def create_book():
    return bookRepository.create(data=request.get_json())


@app.route("/book/<id>", methods=["DELETE"])
def delete_book(id):
    return bookRepository.delete(id)


@app.route("/book/<id>", methods=["PUT"])
def update_book(id):
    return bookRepository.update(id, request.get_json())


@app.route("/books/by")
def get_books_by_author():
    author = request.args.get("author")
    return bookRepository.get_books_by_author(author)


@app.route("/books/by/")
def get_books_by_genre():
    genre = request.args.get("genre")
    return bookRepository.get_books_by_genre(genre)


@app.route("/books/search_by/")
def get_books_by_filter():
    last = request.args.get("last")
    filter = request.args.get("filter")
    param = request.args.get("param")
    return bookRepository.get_books_by_filter(last, filter, param)


@app.route("/books/upload", methods=["POST"])
def upload_file():
    print("fwefwefwrf")
    file = request.files["file"]
    print(file)
    if file and bookRepository.allowed_file(file.filename):
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
    return Response(status=200)


@app.route("/book/download/<id>", methods=["GET"])
def download(id):
    path = bookRepository.download(id)
    return send_file(path, as_attachment=True)


@app.errorhandler(500)
def server_error(e):
    return 'Server error'


@app.errorhandler(400)
def bad_request(e):
    return 'Bad request'
