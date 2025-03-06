from flask import Blueprint, jsonify, request
from app.models.customer_model import Customer
from app.services.add_header import add_header

customer_bp = Blueprint("customer", __name__)


@customer_bp.route("/customers", methods=["GET", "POST"])
def get_all_customers():
    if request.method == "GET":
        customers = Customer.get_all_customer()

        customers = jsonify(customers)
        customers.headers.add("Access-Control-Allow-Origin", "*")

        return customers
    elif request.method == "POST":
        name = request.args["name"]
        address = request.args["address"]
        mobile = request.args["mobile"]
        balance = request.args["balance"]

        print(name, address, mobile, balance)

        cid = Customer.add_customer(name, address, mobile, balance)
        print("Customer created id: ", cid)

        return add_header(cid)


@customer_bp.route("/customer/<int:id>", methods=["GET"])
def get_customer_by_id(id):
    customer = Customer.get_customer_by_id(id)
    customer = add_header(customer)

    return customer
