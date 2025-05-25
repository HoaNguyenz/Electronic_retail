from flask import Blueprint, request, jsonify
from utils.payment import makePayment

payment_bp = Blueprint("payment", __name__)

@payment_bp.route("/payment", methods=["POST"])
def default_payment():
    try:
        data = request.get_json()
        customer_id = data.get("customer_id")
        order_id = data.get("order_id")
        payment_method = data.get("payment_method")
        # Call the payment utility function
        print(customer_id, order_id, payment_method)
        result = makePayment(
            customer_id,
            order_id,
            payment_method
        )
        # Only return success if status is 200
        print(result)
        if result.get("status") == 200:
            return jsonify({"message": "Payment successful", "status": 200}), 200
        else:
            return jsonify(result), result.get("status", 500)
    except Exception as e:
        return jsonify({"error": "An unexpected error occurred", "details": str(e)}), 500