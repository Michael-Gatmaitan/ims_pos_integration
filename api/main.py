from flask import Flask, jsonify, request
from flask_cors import CORS

import mysql.connector
from mysql.connector import Error

from services.db import ims_db, pos_db

# from models.items import get_item_by_id

app = Flask(__name__)
CORS(app)


def setupTriggers():
    db = ims_db()

    cursor = db.cursor(dictionary=True)

    # beforeInsert_trigger_query = """
    # CREATE TRIGGER sample_trigger
    # BEFORE INSERT ON ims_order
    # FOR EACH ROW
    # BEGIN
    # IF NEW.Score < 35
    # THEN SET NEW.Grade = 'FAIL'
    # ELSE SET NEW.Grade = 'PASS'
    # END IF
    # END
    # """

    trigger_sql = """
    DELIMITER //
    CREATE TRIGGER IF NOT EXISTS check_inventory_before_order
    BEFORE INSERT ON ims_order
    FOR EACH ROW
    BEGIN
    
        DECLARE available_quantity INT;
        SELECT quantity INTO available_quantity
        FROM ims_product WHERE pid = CAST(NEW.product_id AS UNSIGNED);
        IF (available_quantity < NEW.total_shipped) THEN
            SIGNAL SQLSTATE '45000'
            SET MESSAGE_TEXT = CONCAT('Insufficient inventory. Available: ', available_quantity, ', Requested: ', NEW.total_shipped);
        ELSE
            UPDATE ims_product SET quantity = quantity - NEW.total_shipped
            WHERE pid = CAST(NEW.product_id AS UNSIGNED);
        END IF;
    END;//

    DELIMITER ;
    """

    cursor.execute(trigger_sql)
    db.commit()
    cursor.close()
    db.close()


# setupTriggers()


def trigger():
    connection = ims_db()
    cursor = connection.cursor(dictionary=True)
    trigger_query = """
    DELIMITER //

    CREATE TRIGGER IF NOT EXISTS check_inventory_before_order
    BEFORE INSERT ON ims_order
    FOR EACH ROW
    BEGIN
        DECLARE available_quantity INT;

        SELECT quantity INTO available_quantity
        FROM ims_product
        WHERE pid = CAST(NEW.product_id AS UNSIGNED);

        IF (available_quantity < NEW.total_shipped) THEN
            SIGNAL SQLSTATE '45000';
        ELSE
            UPDATE ims_product
            SET quantity = quantity - NEW.total_shipped
            WHERE pid = CAST(NEW.product_id AS UNSIGNED);
        END IF;
    END //

    DELIMITER ;
    """

    try:
        # Drop existing trigger to avoid duplicates
        drop_trigger_query = "DROP TRIGGER IF EXISTS check_inventory_before_order"
        cursor.execute(drop_trigger_query)

        # Create new trigger
        cursor.execute(trigger_query)
        connection.commit()

        print("Inventory check trigger created successfully")

    except Error as e:
        print(f"Error creating trigger: {e}")
        connection.rollback()


# trigger()


def addHeaders(result):
    result = jsonify(result)
    result.headers.add("Access-Control-Allow-Origin", "*")

    return result


@app.route("/api/set-trigger", methods=["POST"])
def set_trigger():
    try:
        trigger()
        return "Done setting"
    except Exception as e:
        return addHeaders(
            {
                "status": "error",
                "message": str(
                    e,
                ),
            }
        )


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
# TODO:
# -- Make sure the product deducts
# -- UI should update after query
# -- New order data should be created after updating the stock
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


# Endpoint for dynamic category by id
@app.route("/api/items/<int:itemcode>", methods=["GET", "POST"])
def get_item_by_id(itemcode):
    pass


if __name__ == "__main__":
    app.run(debug=True)
