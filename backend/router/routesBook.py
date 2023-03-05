from flask import jsonify, request, Response
from __main__ import app
from backend.database.cfg import db
from backend.action.BookRepository import BookRepository


@app.route("/books")
def get_books():
    first = request.args.get("first")
    last = request.args.get("last")
    if first is None and last is None:
        return BookRepository(db).get_books(1, BookRepository(db).count())
    if first is None or last is None:
        return Response(400)
    return BookRepository(db).get_books(int(first), int(last))


@app.route("/book/<id>")
def get_book(id):
    return BookRepository(db).search_by_id(id).convert_to_json()


@app.route("/book", methods=["POST"])
def create_book():
    return BookRepository(db).create(data=request.get_json())


@app.route("/book/<id>", methods=["DELETE"])
def delete_book(id):
    return BookRepository(db).delete(id)


@app.route("/book/<id>", methods=["PUT"])
def update_book(id):
    return BookRepository(db).update(id, request.get_json())


@app.route("/books/by")
def get_books_by_author():
    author = request.args.get("author")
    return BookRepository(db).get_books_by_author(author)


@app.route("/books/by/")
def get_books_by_genre():
    genre = request.args.get("genre")
    return BookRepository(db).get_books_by_genre(genre)


@app.route("/books/search_by/")
def get_books_by_filter():
    last = request.args.get("last")
    filter = request.args.get("filter")
    param = request.args.get("param")
    return BookRepository(db).get_books_by_filter(last, filter, param)


@app.errorhandler(500)
def server_error(e):
    return 'Server error'


@app.errorhandler(400)
def bad_request(e):
    return 'Bad request'
