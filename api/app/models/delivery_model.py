from flask import jsonify
from app.services.db import pos_db
from app.models.qrcode.qrcode_model import Qrcode


class Delivery:
    def get_all_deliveries():
        print("GET request for deliveries")
        db = pos_db()

        cursor = db.cursor(dictionary=True)
        cursor.execute("SELECT * from delivers")

        deliveries = cursor.fetchall()
        db.close()

        return deliveries

    def create_delivery(total, customer_id, order_id):
        try:
            db = pos_db()

            cursor = db.cursor(dictionary=True)
            cursor.execute(
                "INSERT into delivers (total, customer_id, order_id) VALUES (%s, %s, %s)",
                (total, customer_id, order_id),
            )

            db.commit()
            did = cursor.lastrowid

            if type(did) is not int:
                print("Something went wrong creating delivery. MODELS")
            else:
                print("Delivery successfully created.")

            # create qrcode
            print(did, order_id, customer_id)
            qrpath = Qrcode.generate_qr_on_order(did, order_id, customer_id)
            # print("PATH: ", generated_qr)

            Qrcode.create_qrdata(did, qrpath)

            created_qr = Qrcode.get_qrdata_by_delivery_id(did)
            print(created_qr)

            # delivery = Delivery.get_delivery_by_id(did)
            # delivery = jsonify(delivery)
            # delivery.headers.add("Access-Control-Allow-Origin", "*")
            cursor.close()

            return did
        except Exception as e:
            print("error has occured in creating delivery with qr", e)
            return e

    def get_delivery_by_id(id):
        db = pos_db()
        cursor = db.cursor(dictionary=True)
        cursor.execute("SELECT * FROM delivers WHERE deliver_id = %s", (id,))
        delivery = cursor.fetchone()

        # delivery = jsonify(delivery)
        # delivery.headers.add("Access-Control-Allow-Origin", "*")
        # delivery = add_header(delivery)

        return delivery
