import requests
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Order service is running"

@app.route("/check-payment")
def check_payment():
    try:
        response = requests.get("http://payments:5000/")
        return f"Payment service response: {response.text}"
    except Exception as e:
        return f"Error contacting payments: {str(e)}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
