from flask import Blueprint, jsonify
from app.models.customer_model import Customer
from app.services.add_header import add_header

customer_bp = Blueprint("customer", __name__)


@customer_bp.route("/customers", methods=["GET"])
def get_all_customers():
    customers = Customer.get_all_customer()

    customers = jsonify(customers)
    customers.headers.add("Access-Control-Allow-Origin", "*")

    return customers


@customer_bp.route("/customer/<int:id>", methods=["GET"])
def get_customer_by_id(id):
    customer = Customer.get_customer_by_id(id)
    customer = add_header(customer)

    return customer
