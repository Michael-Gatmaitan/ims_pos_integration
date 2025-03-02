from flask import Blueprint, request
from app.models.qrcode.qrcode_model import Qrcode
from app.models.delivery_model import Delivery
from app.services.db import pos_db
from app.services.add_header import add_header
import os

qrcode_bp = Blueprint("qrcode", __name__)


@qrcode_bp.route(
    "/qrcode",
    methods=[
        "GET",
    ],
)
def qrcodeget():
    item_code, item_name = Qrcode.get_product_by_camera()
    print("GET")

    if item_code is None:
        return "Nothing here"

    # TODO: 1: check the item_code if its in the database
    # TODO: 2: check the delivery status????
    # WARNING: THERE'S A LOT TO CLEAR IN MY MIND LOL
    return f"{item_code} is here"


@qrcode_bp.route("/create-qrcode", methods=["POST"])
def create_qrcode():
    delivery_id = request.args["delivery_id"]
    qrpath = request.args["qrpath"]

    qrcode_id = Qrcode.create_qrdata(delivery_id, qrpath)

    qrcode = Qrcode.get_qrdata_by_id(qrcode_id)

    qrcode = add_header(qrcode)

    print(f"Created qrcode with id of {qrcode_id}")

    return qrcode_id


@qrcode_bp.route("/qrcode/<int:delivery_id>")
def get_qrcode_by_delivery_id(delivery_id):
    qrcode = Qrcode.get_qrdata_by_id(delivery_id)
    print(qrcode)
    qrcode = add_header(qrcode)

    return qrcode


@qrcode_bp.route("/last-qr", methods=["GET"])
def access_last_qr():
    qrcode = Qrcode.get_last_qr()
    qrcode = add_header(qrcode)

    return qrcode


@qrcode_bp.route("/rider-scan", methods=["GET"])
def rider_scan_qr():
    did, oid, cid = Qrcode.rider_scan_qr()
    # print(res)

    Delivery.updateDelivery(did)

    delivery = Delivery.get_delivery_by_id(did)
    delivery = add_header(delivery)

    return delivery
