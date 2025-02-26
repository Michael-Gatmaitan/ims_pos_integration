from app.services.db import ims_db


class Order:
    @staticmethod
    def get_order_by_id(oid):
        db = ims_db()

        cursor = db.cursor(dictionary=True)
        cursor.execute("SELECT * FROM ims_order WHERE order_id = %s", (oid,))
        order = cursor.fetchone()

        print(order)

        db.close()

        return order
