from flask import jsonify
from app.services.db import pos_db, ims_db
from app.models.product_model import Product
from app.models.order_model import Order
from app.models.sale_model import Sale


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
            print(f"ORDERRRR {order}")

            product = Product.get_product_by_id(pid)

            pdb = pos_db()
            print(product)

            print(product["base_price"] * quantity)
            print(product["base_price"], quantity)

            pcursor = pdb.cursor(dictionary=True)
            pcursor.execute(
                "INSERT INTO sales (sale_value, order_id) VALUES (%s, %s)",
                (product["base_price"] * quantity, order["order_id"]),
            )

            Product.deduct_product_quantity(pid, quantity)

            pdb.commit()

            sale_id = pcursor.lastrowid
            print(sale_id)

            sale = Sale.get_sale_by_id(sale_id)
            print(f"SALEEEEE {sale}")

            response = jsonify(sale)
            response.headers.add("Access-Control-Allow-Origin", "*")

            # close databases
            idb.close()
            pdb.close()

            return response
        except Exception as e:
            return e
