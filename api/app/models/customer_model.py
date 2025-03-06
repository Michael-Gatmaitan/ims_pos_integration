from app.services.db import ims_db


class Customer:
    @staticmethod
    def get_all_customer():
        db = ims_db()

        cursor = db.cursor(dictionary=True)
        cursor.execute("SELECT * FROM ims_customer")
        customers = cursor.fetchall()
        db.close()

        return customers

    def get_customer_by_id(id):
        db = ims_db()

        cursor = db.cursor(dictionary=True)
        cursor.execute("SELECT * FROM ims_customer WHERE id = %s", (id,))
        customer = cursor.fetchone()
        db.close()

        return customer

    def deduct_customer_balance(customer_id, price):
        db = ims_db()

        cursor = db.cursor(dictionary=True)
        # cursor.execute("SELECT * FROM ims_customer WHERE id = %s", (id,))
        # customer = cursor.fetchone()

        cursor.execute(
            "UPDATE ims_customer SET balance = balance - %s WHERE id = %s",
            (price, customer_id),
        )
        db.commit()

        db.close()

        return "Balance deducted"

    def add_customer(name, address, mobile, balance):
        db = ims_db()

        cursor = db.cursor(dictionary=True)
        query = "INSERT INTO ims_customer (name, address, mobile, balance) VALUES (%s, %s, %s, %s)"
        args = (name, address, mobile, balance)
        cursor.execute(query, args)
        db.commit()

        cid = cursor.lastrowid
        db.close()

        return cid
        # cursor
