from flask import Blueprint, request, render_template, jsonify
from app.models.product_model import Product
from app.services.add_header import add_header
from app.models.qrcode.qrcode_model import Qrcode
from app.models.brand_model import Brand

product_bp = Blueprint("products", __name__)


@product_bp.route("/brand")
def get_brands():
    brands = Brand.get_brands()
    brands = add_header(brands)

    return brands


@product_bp.route("/products", methods=["GET"])
def get_products():
    products = Product.get_all_products()
    products = add_header(products)
    return products


@product_bp.route("/products/<int:product_id>", methods=["GET", "DELETE"])
def get_product_by_pid(product_id):
    product = Product.get_product_by_id(product_id)
    print(product)
    product = add_header(product)

    return product


@product_bp.route("/counter")
def counter():
    return render_template("counter.html")


@product_bp.route("/product-list")
def get_all_products():
    return render_template("products.html", title="Michael pogi eehe")


# @product_bp.route
# @product_bp.route("/place-order", methods=["POST"])
# def place_order():
#     # if request.method == "POST":
#     pass
