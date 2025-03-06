from app.services.db import ims_db, pos_db


class Brand:
    @staticmethod
    def get_brands():
        db = ims_db()
        cursor = db.cursor(dictionary=True)
        cursor.execute("SELECT * FROM ims_brand")
        brands = cursor.fetchall()

        # brands = add_header(brands)

        db.close()

        return brands
