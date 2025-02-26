from flask import Blueprint, jsonify
from app.models.customer_model import Customer

customer_bp = Blueprint("customer", __name__)


@customer_bp.route("/customers", methods=["GET"])
def get_all_customers():
    customers = Customer.get_all_customer()

    customers = jsonify(customers)
    customers.headers.add("Access-Control-Allow-Origin", "*")

    return customers
