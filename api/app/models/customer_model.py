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
