from app.qrcode.index import (
    # scan_qr_from_camera,
    test_qr_camera,
    # save_to_csv,
    generate_qr_delivery,
)
import pathlib
from app.services.db import pos_db


class Qrcode:
    @staticmethod
    def get_product_by_camera():
        item_code, item_name = test_qr_camera()
        print(item_code, item_name)

        if item_code is None:
            return None, None

        return item_code, item_name

    def generate_qr_on_order(delivery_id, order_id, customer_id):
        print(pathlib.Path(__file__).parent.resolve())
        try:
            # def get_product_by_path():
            # the data will be based on the deliver id
            path = generate_qr_delivery(delivery_id, order_id, customer_id)

            # print(f"PATH: {path}")
            return path
        except Exception as e:
            print("Error in generate_qr_on_order", e)
            return e

    def create_qrdata(delivery_id, qrpath):
        db = pos_db()
        cursor = db.cursor(dictionary=True)
        cursor.execute(
            "INSERT INTO qrcode (delivery_id, qrpath) VALUES (%s, %s)",
            (delivery_id, qrpath),
        )
        db.commit()

        db.close()

        qrcode_id = cursor.lastrowid

        return qrcode_id

    def get_qrdata_by_delivery_id(delivery_id):
        db = pos_db()
        cursor = db.cursor(dictionary=True)
        # cursor.execute("SELECT * FROM qrcode WHERE qrcode_id = %s", (id,))
        # db.commit()
        #
        # db.close()
        #
        # qrcode_id = cursor.lastrowid

        cursor = db.cursor(dictionary=True)
        cursor.execute(
            "SELECT * FROM qrcode WHERE delivery_id = %s", (delivery_id,))
        qrcode = cursor.fetchone()

        return qrcode

    def get_last_qr():
        db = pos_db()
        cursor = db.cursor(dictionary=True)
        cursor.execute("SELECT * FROM qrcode ORDER BY qrcode_id DESC")
        qrcode = cursor.fetchone()

        return qrcode
