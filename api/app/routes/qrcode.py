from flask import Blueprint
from app.models.qrcode.qrcode_model import Qrcode

qrcode_bp = Blueprint("qrcode", __name__)


@qrcode_bp.route("/qrcode", methods=["GET"])
def qrcodeget():
    item_code, item_name = Qrcode.get_product_by_camera()
    print("GET")

    if item_code is None:
        return "Nothing here"

    # TODO: 1: check the item_code if its in the database
    # TODO: 2: check the delivery status????
    # WARNING: THERE'S A LOT TO CLEAR IN MY MIND LOL
    return f"{item_code} is here"
