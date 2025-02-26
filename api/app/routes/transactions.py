from flask import Blueprint, request
from app.models.transaction_model import Transaction

transaction_bp = Blueprint("transactions", __name__)

# http post http://127.0.0.1:5000/api/place-order?customer_id=1&pid=1&q=3


@transaction_bp.route("/place-order", methods=["POST"])
def place_order():
    cid = int(request.args.get("customer_id"))
    pid = int(request.args.get("pid"))
    q = int(request.args.get("q"))

    print(cid, pid, q)

    # return f"${cid} ${pid} ${q}"

    sale = Transaction.place_order(cid, pid, q)
    return sale
