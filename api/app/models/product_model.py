# from flask import jsonify
from app.services.db import ims_db


class Product:
    @staticmethod
    def get_all_products():
        db = ims_db()

        cursor = db.cursor(dictionary=True)
        cursor.execute("SELECT * FROM ims_product")
        items = cursor.fetchall()
        db.close()

        # response = jsonify(items)
        # response.headers.add("Access-Control-Allow-Origin", "*")

        return items

    def get_product_by_id(id):
        db = ims_db()

        cursor = db.cursor(dictionary=True)
        cursor.execute("SELECT * FROM ims_product WHERE pid = %s", (id,))
        product = cursor.fetchone()
        db.close()

        return product

    def delete_product_by_id(id):
        db = ims_db()

        cursor = db.cursor(dictionary=True)
        cursor.execute("DELETE from ims_product where pid = %s", (id,))
        product = cursor.fetchone()

        db.close()

        return product

    def deduct_product_quantity(pid, quantity):
        db = ims_db()

        print(pid, quantity)

        cursor = db.cursor(dictionary=True)
        cursor.execute(
            "UPDATE ims_product SET quantity = quantity - %s WHERE pid = %s",
            (quantity, pid),
        )

        db.commit()

        db.close()

        print("After deduct")

        return "neh"

    def create_product(pid, pname):
        pass
