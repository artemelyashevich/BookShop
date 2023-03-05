from __main__ import app, db

from flask import request

from backend.action.PurchaseRepository import PurchaseRepository


@app.route("/purchases")
def get_purchases():
    return PurchaseRepository(db).get_all_purchases()


@app.route("/purchase", methods=["POST"])
def create_purchase():
    return PurchaseRepository(db).create_purchase(request.get_json())


@app.route("/purchase/<id>")
def show_purchase(id):
    return PurchaseRepository(db).get_purchase(id)


@app.route("/purchase/by_user/<id>")
def show_purchase_by_user(id):
    return PurchaseRepository(db).get_purchase_by_user(id)
