from flask import jsonify
from app.services.db import pos_db


class Sale:
    @staticmethod
    def get_all_sales():
        db = pos_db()

        cursor = db.cursor(dictionary=True)
        cursor.execute("SELECT * FROM sales")
        sales = cursor.fetchall()
        db.close()

        sales = jsonify(sales)
        sales.headers.add("Access-Control-Allow-Origin", "*")

        return sales

    def get_sale_by_id(sid):
        db = pos_db()

        cursor = db.cursor(dictionary=True)
        cursor.execute("SELECT * FROM sales WHERE sale_id = %s", (sid,))
        sale = cursor.fetchone()
        db.close()

        return sale
