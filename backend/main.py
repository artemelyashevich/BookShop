from flask import Flask
from flask_cors import CORS

from backend.action.BookRepository import UPLOAD_FOLDER
from backend.database.cfg import db

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.app_context().push()
db.init_app(app)

CORS(app)

from pcgs import *

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
