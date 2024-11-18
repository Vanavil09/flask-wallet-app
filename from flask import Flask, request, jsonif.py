from flask import Flask, request, jsonify

app = Flask(__name__)

# Mock wallet data
wallet_balance = {"my_wallet": 100.0}  # Initial balance

@app.route('/wallet_balance', methods=['GET'])
def get_wallet_balance():
    return jsonify({"balance": wallet_balance["my_wallet"]})

@app.route('/transfer', methods=['POST'])
def transfer_money():
    data = request.json
    upi_id = data.get("upi_id")
    amount = data.get("amount")

    if not upi_id or not amount:
        return jsonify({"error": "UPI ID and amount are required"}), 400

    if amount > wallet_balance["my_wallet"]:
        return jsonify({"error": "Insufficient wallet balance"}), 400

    # Deduct amount from wallet
    wallet_balance["my_wallet"] -= amount

    # Simulate transfer success
    return jsonify({
        "message": f"₹{amount} transferred to {upi_id} successfully.",
        "remaining_balance": wallet_balance["my_wallet"]
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
