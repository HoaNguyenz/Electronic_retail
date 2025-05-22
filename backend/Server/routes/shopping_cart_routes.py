from flask import Blueprint, request, jsonify
from utils.shopping_cart import add_product_to_cart, update_cart_item, remove_product_from_cart

shopping_cart_bp = Blueprint("shoppingcart", __name__)

@shopping_cart_bp.route("/shoppingcart/add", methods=["POST"])
def add_to_cart():
    try:
        data = request.json
        required_fields = ["customer_id", "product_id", "quantity", "order_id"]
        if not data or not all(field in data for field in required_fields):
            return jsonify({"error": "Invalid input"}), 400

        response = add_product_to_cart(data["customer_id"], data["order_id"], data["product_id"], data["quantity"])
        return jsonify(response), response.get("status", 500)
    except Exception as e:
        return jsonify({"error": "An unexpected error occurred", "details": str(e)}), 500

@shopping_cart_bp.route("/shoppingcart/update", methods=["POST"])
def update_cart():
    try:
        data = request.json
        required_fields = ["order_item_id", "quantity"]
        if not data or not all(field in data for field in required_fields):
            return jsonify({"error": "Invalid input"}), 400

        response = update_cart_item(data["order_item_id"], data["quantity"])
        return jsonify(response), response.get("status", 500)
    except Exception as e:
        return jsonify({"error": "An unexpected error occurred", "details": str(e)}), 500

@shopping_cart_bp.route("/shoppingcart/remove", methods=["POST"])
def remove_from_cart():
    try:
        data = request.json
        required_fields = ["order_item_id"]
        if not data or not all(field in data for field in required_fields):
            return jsonify({"error": "Invalid input"}), 400

        response = remove_product_from_cart(data["order_item_id"])
        return jsonify(response), response.get("status", 500)
    except Exception as e:
        return jsonify({"error": "An unexpected error occurred", "details": str(e)}), 500