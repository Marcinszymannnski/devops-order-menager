from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import OperationalError
import time 
import os

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
db = SQLAlchemy(app)

class Payment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String(20), nullable=False)

@app.route("/")
def home():
    return "Payment service is running, działa"

@app.route("/payment", methods=["POST"])
def create_payment():
    data = request.json
    new_payment = Payment(order_id=data["order_id"], status=data["status"])
    db.session.add(new_payment)
    db.session.commit()
    return jsonify({"message": "Payment created", "payment_id": new_payment.id})

@app.route("/payment/<int:payment_id>", methods=["GET"])
def get_payment(payment_id):
    payment = Payment.query.get(payment_id)
    if payment:
        return jsonify({"order_id": payment.order_id, "status": payment.status})
    return jsonify({"error": "Payment not found"}), 404

if __name__ == "__main__":

    connected = False
    for _ in range(10):  
        try:
            with app.app_context():
                db.create_all()
            connected = True
            print("Połączono z bazą danych")
            break
        except OperationalError as e:
            print("Baza jeszcze niedostępna, ponawiam próbę...")
            time.sleep(2)
    
    if not connected:
        print("Nie udało się połączyć z bazą danych")
        exit(1)

    app.run(host="0.0.0.0", port=5000)
