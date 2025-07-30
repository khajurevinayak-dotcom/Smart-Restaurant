from flask import Flask, request, jsonify

app = Flask(__name__)

orders = []  # store orders in memory for now

@app.route("/")
def home():
    return "✅ Smart Restaurant Backend Running!"

@app.route("/place_order", methods=["POST"])
def place_order():
    data = request.json
    orders.append(data)
    print("📦 New Order:", data)
    return jsonify({"status": "success", "message": "Order saved!"})

@app.route("/view_orders", methods=["GET"])
def view_orders():
    return jsonify(orders)

if __name__ == "__main__":
    app.run(debug=True)