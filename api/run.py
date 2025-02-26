from flask import Flask
from app.routes.products import product_bp
from app.routes.customers import customer_bp
from app.routes.transactions import transaction_bp
from app.routes.orders import order_bp
from app.routes.sales import sale_bp
from app.routes.deliveries import delivery_bp

app = Flask(__name__)
app.register_blueprint(product_bp, url_prefix="/api")
app.register_blueprint(customer_bp, url_prefix="/api")
app.register_blueprint(transaction_bp, url_prefix="/api")
app.register_blueprint(order_bp, url_prefix="/api")
app.register_blueprint(sale_bp, url_prefix="/api")
app.register_blueprint(delivery_bp, url_prefix="/api")


if __name__ == "__main__":
    app.run(debug=True)
