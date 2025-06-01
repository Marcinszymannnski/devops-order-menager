from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy  
import os

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
db = SQLAlchemy(app)

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    item = db.Column(db.String(80), nullable=False)
    price = db.Column(db.Float, nullable=False)

@app.route("/")
def home():
    return "Order service is running, działa"

@app.route("/order", methods=["POST"])
def create_order():
    data = request.json
    new_order = Order(item=data["item"], price=data["price"])
    db.session.add(new_order)
    db.session.commit()
    return jsonify({"message": "Order created", "order_id": new_order.id})

@app.route("/order/<int:order_id>", methods=["GET"])
def get_order(order_id):
    order = Order.query.get(order_id)
    if order:
        return jsonify({"item": order.item, "price": order.price})
    return jsonify({"error": "Order not found"}), 404

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(host="0.0.0.0", port=5000)
