from flask import Flask, jsonify, request
from flask_cors import CORS

import mysql.connector

from db import ims_db, pos_db

# from models.items import get_item_by_id

app = Flask(__name__)
CORS(app)


def addHeaders(result):
    result = jsonify(result)
    result.headers.add("Access-Control-Allow-Origin", "*")

    return result


@app.route("/api/products", methods=["GET"])
def get_items():
    db = ims_db()

    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM ims_product")
    items = cursor.fetchall()
    cursor.close()
    db.close()

    response = jsonify(items)
    response.headers.add("Access-Control-Allow-Origin", "*")

    return response


# http post "http://127.0.0.1:5000/api/update-stock?pid=3&deduct_value=2"
@app.route("/api/update-stock", methods=["POST"])
def handle_update_stock():
    if request.method == "POST":
        try:
            deduct_value = request.args.get("deduct_value")
            product_id = request.args.get("pid")
            add_value = request.args.get("add_value")

            db = ims_db()
            cursor = db.cursor(dictionary=True)

            if deduct_value is None and add_value is None:
                return ""

            if deduct_value is not None:
                # deduct the product quantity
                query = "UPDATE ims_product SET quantity = quantity - %s WHERE pid = %s"

            elif add_value is not None:
                # add value to product quantity
                query = "UPDATE ims_product SET quantity = quantity + %s WHERE pid = %s"

            data = (deduct_value, product_id)
            cursor.execute(query, data)
            db.commit()

            cursor.execute("SELECT * FROM ims_product WHERE pid = %s", (product_id,))

            items = cursor.fetchone()
            items = addHeaders(items)

            cursor.close()
            db.close()

            return items

        except mysql.connector.Error as err:
            print(f"Error: {err}")


if __name__ == "__main__":
    app.run(debug=True)
