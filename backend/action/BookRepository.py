from flask import jsonify, abort, Response

from backend.model.Book import Book


class BookRepository:

    def __init__(self, db):
        self.db = db
        self.books = self.db.session.query(Book).all()

    def get_books(self, first, last):
        count = last - first
        data = []
        for i in range(count + 1):
            book = self.search_by_id(first + i)
            data.append({
                "id": book.id,
                "title": book.title,
                "author": book.author,
                "price": book.price
            })
        return jsonify(data)

    def get_books_by_author(self, author):
        data = []
        for book in self.books:
            if book.author == author:
                data.append({
                    "id": book.id,
                    "title": book.title,
                    "author": book.author,
                    "price": book.price,
                    "category": book.category})
        return data

    def get_books_by_genre(self, genre):
        data = []
        for book in self.books:
            if book.category == genre:
                data.append({
                    "id": book.id,
                    "title": book.title,
                    "author": book.author,
                    "price": book.price,
                    "category": book.category})
        return data

    def get_books_by_filter(self, last, filter, param):
        try:
            if filter == "category":
                print("+")
                data = []
                print(len(self.get_books_by_genre(param)))
                if len(self.get_books_by_genre(param)) > int(last):
                    for i in range(0, int(last)):
                        print(self.get_books_by_genre(param)[i])
                        data.append(self.get_books_by_genre(param)[i])
                        return data
                else:
                    return self.get_books_by_genre(param)
            else:
                print("-")
                data = []
                print(len(self.get_books_by_author(param)))
                if len(self.get_books_by_author(param)) > int(last):
                    for i in range(0, int(last)):
                        data.append(self.get_books_by_author(param)[i])
                else:
                    return self.get_books_by_author(param)
        except Exception as e:
            print(e)
            Response(status=500)

    def update(self, id, data):
        if self.check_data(data):
            abort(400)
        try:
            book = self.search_by_id(int(id))

            book.title = data["title"]
            book.author = data["author"]
            book.price = data["price"]
            book.category = data["category"]

            self.db.session.commit()

        except Exception as e:
            print(e)
            abort(500)

        return Response(status=200)

    def create(self, data):
        if self.check_data(data):
            abort(400)

        try:
            book = Book(
                title=data["title"],
                author=data["author"],
                category=data["category"],
                price=data["price"]
            )
            self.db.session.add(book)
            self.db.session.commit()

        except Exception as e:
            print(e)
            abort(500)
        return Response(status=200)

    def search_by_id(self, _id):
        return self.db.session.query(Book).filter_by(id=_id).first()

    def delete(self, id):
        if id == "":
            abort(400)
        try:
            if id.isdigit():
                self.db.session.delete(self.search_by_id(id))
                self.db.session.commit()
                return Response(status=200)
        except Exception as e:
            print(e)
            abort(500)

    def count(self):
        return len(self.db.session.query(Book).all())

    @staticmethod
    def check_data(data):
        if (data["title"] == '') or (data["author"] == '') \
                or (data["price"] == '') or (data["category"] == ''):
            return True
        elif (data["title"] is None) or (data["author"] is None) \
                or (data["price"] is None) or (data["category"] is None):
            return True
