from flask import jsonify
from app.services.db import pos_db, ims_db
from app.models.product_model import Product
from app.models.order_model import Order
from app.models.sale_model import Sale
from app.models.delivery_model import Delivery


class Transaction:
    @staticmethod
    def place_order(customer_id, pid, quantity):
        try:
            print(customer_id, pid, quantity)

            idb = ims_db()
            icursor = idb.cursor(dictionary=True)
            icursor.execute(
                "INSERT INTO ims_order (product_id, total_shipped, customer_id) VALUES (%s, %s, %s)",
                (pid, quantity, customer_id),
            )
            idb.commit()
            # order = icursor.fetchone()
            oid = icursor.lastrowid

            order = Order.get_order_by_id(oid)

            product = Product.get_product_by_id(pid)

            pdb = pos_db()
            print(product)

            sale_value = product["base_price"] * quantity

            print(f"{product['base_price']} * {quantity} = {sale_value}")

            Product.deduct_product_quantity(pid, quantity)

            # Create a delivery data also after creating sales
            Delivery.create_delivery(
                sale_value, customer_id, order["order_id"])

            sale_id = Sale.create_sale(sale_value, order["order_id"])
            print(sale_id)

            sale = Sale.get_sale_by_id(sale_id)
            print(f"SALEEEEE {sale}")

            # close databases
            idb.close()
            pdb.close()

            return sale
        except Exception as e:
            print("error has occured")
            print(e)
            return e
