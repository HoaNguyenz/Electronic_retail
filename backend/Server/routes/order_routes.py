from flask import Blueprint, request, jsonify
from utils.order import process_order, cancel_order, get_order_data, get_order_history

order_bp = Blueprint("order", __name__)

@order_bp.route("/order/fetch", methods=["GET"])
def fetch_order():
    try:
        # Get request data
        order_id = request.args.get("order_id")
        customer_id = request.args.get("customer_id")

        if not order_id or not customer_id:
            return jsonify({"error": "Missing order_id or customer_id", "status": 400})
        # Call the fetch_order function
        result = get_order_data(order_id, customer_id)
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": "Unexpected server error", "details": str(e), "status": 500})
    
@order_bp.route("/order/checkout", methods=["POST"])
def place_order():
    try:
        # Get request data
        data = request.get_json()
        customer_id = data.get("customer_id")
        payment_method = data.get("payment_method")
        order_id = data.get("order_id")

        if not customer_id or not payment_method:
            return jsonify({"error": "Missing customer_id or payment_method", "status": 400})

        # Call the process_order function
        result = process_order(customer_id, order_id, payment_method)

        return jsonify(result)

    except Exception as e:
        return jsonify({"error": "Unexpected server error", "details": str(e), "status": 500})

@order_bp.route("/order/cancel", methods=["POST"])
def cancel_order():
    try:
        # Get request data
        data = request.get_json()
        order_id = data.get("order_id")
        customer_id = data.get("customer_id")

        if not order_id or not customer_id:
            return jsonify({"error": "Missing order_id or customer_id", "status": 400})

        # Call the cancel_order function
        result = cancel_order(order_id)

        return jsonify(result)
    except Exception as e:
        return jsonify({"error": "Unexpected server error", "details": str(e), "status": 500})
    
@order_bp.route("/order/history", methods=["GET"])
def order_his():
    try:
        # Get request data
        customer_id = request.args.get("customer_id")
        
        if not customer_id:
            return jsonify({"error": "Missing customer_id", "status": 400})
        
        result = get_order_history(customer_id)
        
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": "Unexpected server error", "details": str(e), "status": 500})
    
        