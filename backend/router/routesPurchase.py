from __main__ import app, db

from flask import request

from backend.action.PurchaseRepository import PurchaseRepository

purchaseRepository = PurchaseRepository(db)


@app.route("/purchases")
def get_purchases():
    return purchaseRepository.get_all_purchases()


@app.route("/purchase", methods=["POST"])
def create_purchase():
    return purchaseRepository.create_purchase(request.get_json())


@app.route("/purchase/<id>")
def show_purchase(id):
    return purchaseRepository.get_purchase(id)


@app.route("/purchase/by_user/<id>")
def show_purchase_by_user(id):
    return purchaseRepository.get_purchase_by_user(id)


@app.errorhandler(500)
def server_error(e):
    return 'Server error'


@app.errorhandler(400)
def bad_request(e):
    return 'Bad request'
