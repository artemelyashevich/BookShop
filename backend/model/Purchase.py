from datetime import datetime

from backend.database.cfg import db


class Purchase(db.Model):
    __tablename__ = 'purchase'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    id_user = db.Column(db.Integer, db.ForeignKey('user.id'))
    id_book = db.Column(db.Integer, db.ForeignKey('book.id'))
    date = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, id_user, id_book):
        self.id_user = id_user
        self.id_book = id_book

    def __repr__(self):
        return "Purchase id:  " + str(self.id) + "\nUser_id: " + str(self.id_user) + "\nBook_id: " + str(self.id_book)
