# from flask import jsonify
from flask import request
from app.services.db import ims_db


class Product:
    @staticmethod
    def get_all_products():
        db = ims_db()

        cursor = db.cursor(dictionary=True)
        cursor.execute("SELECT * FROM ims_product")
        items = cursor.fetchall()
        db.close()

        return items

    def get_product_by_id(id):
        db = ims_db()

        cursor = db.cursor(dictionary=True)
        cursor.execute("SELECT * FROM ims_product WHERE pid = %s", (id,))
        product = cursor.fetchone()
        db.close()

        return product

    # def add_product_using_qr(item_code, item_name):
    # qrcode_generator()

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
        db = ims_db()

        cursor = db.cursor(dictionary=True)

        cursor.execute("INSERT INTO ims_product VALUES (%s, %s)", (pname,))
        db.commit()
        db.close()
        pass
