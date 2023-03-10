from flask import Response, jsonify
from backend.model.Purchase import Purchase


class PurchaseRepository:
    def __init__(self, db):
        self.db = db
        self.purchases = self.db.session.query(Purchase).all()

    def get_all_purchases(self):
        data = []
        for p in self.purchases:
            data.append({
                "id": p.id,
                "id_user": p.id_user,
                "id_book": p.id_book
            })
        return data

    def create_purchase(self, data):
        if self.check_data(data):
            return Response(status=400)
        try:
            p = Purchase(id_user=data["id_user"], id_book=data["id_book"])
            self.db.session.add(p)
            self.db.session.commit()
        except Exception as e:
            print(e)
            return Response(status=500)
        return Response(status=200)

    def get_purchase(self, id):
        data = []
        try:
            for p in self.purchases:
                if int(id) == int(p.id):
                    return jsonify({
                        "id": p.id,
                        "id_user": p.id_user,
                        "id_book": p.id_book
                    })
        except Exception as e:
            print(e)
            return Response(status=400)
        return Response(500)

    def get_purchase_by_user(self, id):
        data = []
        for p in self.purchases:
            if id == p.id_user:
                data.append({
                    "id": p.id,
                    "id_user": p.id_user,
                    "id_book": p.id_book
                })
        return jsonify(data)

    @staticmethod
    def check_data(data):
        if data["id_user"] == 0 or data["id_book"] == 0:
            return True
        if data["id_user"] is None or data["id_book"] is None:
            return True
