from flask import Blueprint
from app.models.order_model import Order
from app.services.add_header import add_header

order_bp = Blueprint("order", __name__)


@order_bp.route("/order/<int:order_id>", methods=["GET"])
def get_order_by_id(order_id):
    order = Order.get_order_by_id(order_id)
    order = add_header(order)

    return order
