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

    def create_sale(sale_value, order_id):
        db = pos_db()
        cursor = db.cursor(dictionary=True)
        cursor.execute(
            "INSERT INTO sales (sale_value, order_id) VALUES (%s, %s)",
            (sale_value, order_id),
        )

        db.commit()

        sale_id = cursor.lastrowid

        return sale_id
