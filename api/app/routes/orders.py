from flask import Blueprint
from app.models.order_model import Order

order_bp = Blueprint("order", __name__)


@order_bp.route("/order/<int:order_id>", methods=["GET"])
def get_order_by_id(order_id):
    order = Order.get_order_by_id(order_id)
    print(order)
    return order
