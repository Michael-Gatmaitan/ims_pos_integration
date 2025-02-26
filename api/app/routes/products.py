from flask import Blueprint, request, render_template, jsonify
from app.models.product_model import Product

product_bp = Blueprint("products", __name__)


@product_bp.route("/products", methods=["GET"])
def get_products():
    products = Product.get_all_products()
    print(products)

    products = jsonify(products)
    products.headers.add("Access-Control-Allow-Origin", "*")

    return products


@product_bp.route("/product-list")
def get_all_products():
    return render_template("products.html", title="Michael pogi eehe")


# @product_bp.route("/place-order", methods=["POST"])
# def place_order():
#     # if request.method == "POST":
#     pass


@product_bp.route("/products/<int:product_id>", methods=["GET", "DELETE"])
def get_product_by_pid(product_id):
    product = Product.get_product_by_id(product_id)
    print(product)

    return product
    # if request.method == "GET":
    #     product = Product.get_product_by_id(pid)
    #
    #     return (
    #         jsonify(product) if product else jsonify({"error": "product not exists."})
    #     )
    #
    # elif request.method == "DELETE":
    #     product = Product.delete_product_by_id(pid)
    #     return jsonify(product)
    if request.method == "GET":
        return render_template("products.html")


@product_bp.route("/counter")
def counter():
    return render_template("counter.html")


# @product_bp.route
