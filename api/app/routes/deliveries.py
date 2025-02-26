from flask import Blueprint
# from app.models.delivery_model import Delivery

delivery_bp = Blueprint("delivery", __name__)


@delivery_bp.route("/delivery", methods=["GET"])
def get_deliveries():
    return "DELIVERY WAHAHA"
