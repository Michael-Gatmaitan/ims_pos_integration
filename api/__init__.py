from flask import Flask, jsonify, request
from flask_cors import CORS

# from flask_mysqldb import MySQL
# from db import db
# from db import inventory_db, pos_db

from db import ims_db, pos_db

# from models.items import get_item_by_id

app = Flask(__name__)
CORS(app)


@app.route("/", methods=["GET", "POST"])
def starting_endpoint():
    return "Hi, im Michael Gatmaitan ^^"


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


@app.route("/api/add_product", methods=["POST"])
def handle_add_item():
    if request.method == "POST":
        print("Create a new item")
        db = ims_db()

        # get url arguments
        # description = request.args["item_description"]

        # item_description = request.args["item_description"]
        # item_unitprice = request.args["item_unitprice"]
        # item_quantity = request.args["item_quantity"]

        cursor = db.cursor(dictionary=True)
        # query = """INSERT INTO items (item_description, item_unitprice, item_quantity)
        # VALUES (%s, %s, %s)"""

        # record = (item_description, float(item_unitprice), float(item_quantity))

        # cursor.execute(query, record)
        # cursor.execute(query)

        db.commit()
        print(cursor.rowcount)
        cursor.close()

        # createdItem = cursor.fetchall()
        # print(createdItem)
        #
        # response = jsonify(createdItem)
        # response.headers.add("Access-Control-Allow-Origin", "*")

        # return jsonify("added")
        return str(cursor.rowcount)


@app.route("/api/items/<int:itemcode>", methods=["GET", "POST"])
def get_item_by_id(itemcode):
    if request.method == "GET":
        db = ims_db()

        cursor = db.cursor(dictionary=True)
        query = "SELECT * FROM items WHERE itemcode = %s"
        args = (itemcode,)
        cursor.execute(query, args)
        item = cursor.fetchall()

        response = jsonify(item)
        response.headers.add("Access-Control-Allow-Origin", "*")

        return response


# Routes for users
@app.route("/api/users", methods=["GET", "POST"])
def get_users():
    if request.method == "GET":
        # db = pos_db()
        db = ims_db()

        cursor = db.cursor(dictionary=True)
        query = "SELECT * FROM users"
        cursor.execute(query)
        items = cursor.fetchall()

        response = jsonify(items)
        response.headers.add("Access-Control-Allow-Origin", "*")

        return response
    elif request.method == "POST":
        db = ims_db()

        firstname = request.args["firstname"]
        lastname = request.args["lastname"]

        # query = """INSERT INTO items (item_description, item_unitprice, item_quantity)
        # VALUES (%s, %s, %s)"""
        query = """INSERT INTO users (first_name, last_name) VALUES (%s, %s)"""
        user_r = (firstname, lastname)

        cursor = db.cursor(dictionary=True)
        cursor.execute(query, user_r)

        db.commit()
        cursor.close()

        print(cursor)
        return "User created"


# Routes for orders
@app.route("/api/orders", methods=["POST"])
def create_order():
    if request.method == "POST":
        _pos_db = pos_db()
        _inv_db = ims_db()

        # test
        # http post "http://127.0.0.1:5000/api/orders?user_id=3&itemcode=3&payment=1000&order_quantity=1"

        # Args
        user_id = request.args["user_id"]
        itemcode = request.args["itemcode"]
        payment = request.args["payment"]
        order_quantity = request.args["order_quantity"]

        payment = float(payment)
        order_quantity = int(order_quantity)

        # check for quantity
        p_cursor = _pos_db.cursor(dictionary=True)

        i_cursor = _inv_db.cursor(dictionary=True)

        item_quantity_q = "SELECT item_quantity from items WHERE itemcode = %s"
        itemcode_r = (itemcode,)

        i_cursor.execute(item_quantity_q, itemcode_r)
        item_quantity = i_cursor.fetchall()
        item_quantity = item_quantity[0]["item_quantity"]

        if item_quantity < order_quantity:
            print("Invalid")
            return "Invalid range of quantity"
        else:
            # process order
            # update item
            new_quantity = item_quantity - order_quantity
            query = "UPDATE items SET item_quantity = %s WHERE itemcode = %s"
            q_args = (new_quantity, itemcode)

            # execute
            i_cursor.execute(query, q_args)

            _inv_db.commit()
            i_cursor.close()

            # Them create a order
            print(user_id, p_cursor)

            return "Done"
        # return str(item_quantity[0]["item_quantity"])


# integrate


if __name__ == "__main__":
    app.run(debug=True)
