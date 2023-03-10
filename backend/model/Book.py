from flask import jsonify
from backend.database.cfg import db


class Book(db.Model):
    __tablename__ = 'book'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, unique=True, nullable="False")
    author = db.Column(db.String, nullable=False)
    price = db.Column(db.Float, nullable=False)
    category = db.Column(db.String)
    img = db.Column(db.String, nullable=True,
                    default="C:\\Users\\37529\\PycharmProjects\\BookShop\\backend\\action\\path\\to\\the\\uploads\\photo_2023-01-28_15-50-29.jpg")

    def __init__(self, title, author, price, category):
        self.title = title
        self.author = author
        self.price = price
        self.category = category

    def convert_to_json(self):
        return jsonify(
            {
                "id": self.id,
                "title": self.title,
                "author": self.author,
                "price": str(self.price),
                "category": self.category,
                "img": self.img
            }
        )

    def set_title(self, title):
        self.title = title

    def set_author(self, author):
        self.author = author

    def set_price(self, price):
        self.price = price

    def set_category(self, category):
        self.category = category

    def set_img(self, img):
        self.img = img

    def __repr__(self):
        return str(self.title)
