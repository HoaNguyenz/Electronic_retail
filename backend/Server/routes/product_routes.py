from flask import Blueprint, request, jsonify
from utils.product import fetch_products

product_bp = Blueprint("product", __name__)

@product_bp.route("/products", methods=["GET"])
def get_products():
    try:
        category_id = request.args.get("category_id")
        min_price = request.args.get("min_price")
        max_price = request.args.get("max_price")
        brand = request.args.get("brand")
        rating = request.args.get("rating")

        result = fetch_products(category_id, min_price, max_price, brand, rating)
        
        if result["success"]:
            return jsonify({"products": result["products"]}), 200
        else:
            return jsonify({"error": result["error"]}), 500

    except Exception as e:
        return jsonify({"error": "An unexpected error occurred", "details": str(e)}), 500
