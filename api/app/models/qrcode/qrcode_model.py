from flask import jsonify
from app.qrcode.index import scan_qr_from_camera, test_qr_camera, save_to_csv


class Qrcode:
    @staticmethod
    def get_product_by_camera():
        item_code, item_name = test_qr_camera()
        print(item_code, item_name)

        if item_code is None:
            return None, None

        return item_code, item_name

    # def get_product_by_path():
    #
