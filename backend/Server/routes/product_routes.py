from flask import Blueprint, request, jsonify
from utils.product import fetch_products, rate_product

product_bp = Blueprint("product", __name__)

@product_bp.route("/products", methods=["GET"])
def get_products():
    try:
        category_id = request.args.get("category_id", type=int)
        min_price = request.args.get("min_price", type=float)
        max_price = request.args.get("max_price", type=float)
        brand = request.args.get("brand")
        rating = request.args.get("rating", type=float)

        result = fetch_products(category_id, min_price, max_price, brand, rating)
        if result["success"]:
            return jsonify({"products": result["products"]}), 200
        else:
            return jsonify({"error": result["error"]}), 400
    except Exception as e:
        return jsonify({"error": "An unexpected error occurred", "details": str(e)}), 500

@product_bp.route("/products/rating/", methods=["POST"])
def post_rating():
    try:
        data = request.get_json()
        product_id = data.get("product_id")
        customer_id = data.get("customer_id")
        rating = data.get("rating")
        comment = data.get("comment")

        if not product_id or not customer_id or rating is None:
            return jsonify({"error": "Missing required fields"}), 400

        try:
            product_id = int(product_id)
            customer_id = int(customer_id)
            rating = int(rating)
        except Exception:
            return jsonify({"error": "Invalid data type for product_id, customer_id, or rating"}), 400

        result = rate_product(product_id, customer_id, rating, comment)
        if result["success"]:
            return jsonify({"message": result["message"]}), 200
        else:
            return jsonify({"error": result["error"]}), 400
    except Exception as e:
        return jsonify({"error": "An unexpected error occurred", "details": str(e)}), 500