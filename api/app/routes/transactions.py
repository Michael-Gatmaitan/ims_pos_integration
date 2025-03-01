from flask import Blueprint, request
from app.models.transaction_model import Transaction
from app.models.customer_model import Customer
from app.models.product_model import Product
from app.services.add_header import add_header

transaction_bp = Blueprint("transactions", __name__)

# http post http://127.0.0.1:5000/api/place-order?customer_id=1&pid=1&q=3


@transaction_bp.route("/place-order", methods=["POST"])
def place_order():
    cid = int(request.args.get("customer_id"))
    pid = int(request.args.get("pid"))
    q = int(request.args.get("q"))

    product = Product.get_product_by_id(pid)
    customer = Customer.get_customer_by_id(cid)

    if customer["balance"] < product["base_price"]:
        print("no no no")
        return add_header({"error": "User balance is too low."})

    print("Place order info", cid, pid, q)

    sale = Transaction.place_order(cid, pid, q)

    Customer.deduct_customer_balance(cid, product["base_price"])

    sale = add_header(sale)

    print("SALE FROM PLACE_ORDER", sale)

    return sale
