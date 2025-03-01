from flask import Blueprint, request
from app.models.sale_model import Sale


sale_bp = Blueprint("sales", __name__)


@sale_bp.route("/sales", methods=["GET", "POST"])
def get_sales():
    if request.method == "GET":
        sales = Sale.get_all_sales()
        return sales


@sale_bp.route("/sale/<int:sale_id>", methods=["GET"])
def get_sale_by_id(sale_id):
    sale = Sale.get_sale_by_id(sale_id)
    print(sale)
    return sale
