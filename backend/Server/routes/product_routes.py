from flask import Blueprint, request, jsonify
from utils.product import *
product_bp = Blueprint("product", __name__)

@product_bp.route("/products", methods=["GET"])
def get_products():
    try:
        category_id = request.args.get("category_id", type=int)
        category_name = request.args.get("category_name")
        min_price = request.args.get("min_price", type=float)
        max_price = request.args.get("max_price", type=float)
        brand = request.args.get("brand")
        rating = request.args.get("rating", type=float)

        result = fetch_products(category_id, min_price, max_price, brand, rating,category_name)
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
    
@product_bp.route("/products/categories", methods=["GET"])
def get_categories():
    try:
        categories = fetch_categories()
        if categories:
            return jsonify({"categories": categories}), 200
        else:
            return jsonify({"error": "No categories found"}), 404
    except Exception as e:
        return jsonify({"error": "An unexpected error occured", "details": str(e)}), 500
    
@product_bp.route("/products/marketing", methods=["GET"])
def get_marketing_imgs():
    try:
        links = get_product_imgs()
        if links:
            return jsonify({"links": links}), 200
        else:
            return jsonify({"error": "No imgs found"}), 404
    except Exception as e:
        return jsonify({"error": "An unexpected error occured", "details": str(e)}), 500
    
@product_bp.route("/product", methods=["GET"])
def get_product():
    try:
        product_id = request.args.get("product_id", type=int)

        result = get_product_detail(product_id)
        if result["success"]:
            return jsonify({"product": result["product"]}), 200
        else:
            return jsonify({"error": result["error"]}), 400
    except Exception as e:
        return jsonify({"error": "An unexpected error occurred", "details": str(e)}), 500