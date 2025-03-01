from flask import Blueprint, request
from app.models.delivery_model import Delivery
from app.services.add_header import add_header

delivery_bp = Blueprint("delivery", __name__)


@delivery_bp.route("/delivery", methods=["GET", "POST"])
def get_deliveries():
    if request.method == "POST":
        # Create a delivery
        total = request.args["total"]
        customer_id = request.args["customer_id"]
        order_id = request.args["order_id"]

        id = Delivery.create_delivery(total, customer_id, order_id)

        delivery = Delivery.get_delivery_by_id(id)

        return delivery
    elif request.method == "GET":
        deliveries = Delivery.get_all_deliveries()
        deliveries = add_header(deliveries)
        return deliveries

    return "DELIVERY WAHAH"


@delivery_bp.route("/delivery/<int:id>", methods=["GET"])
def get_delivery_by_id(id):
    delivery = Delivery.get_delivery_by_id(id)
    return delivery
