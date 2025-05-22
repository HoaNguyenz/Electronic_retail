from flask import Blueprint, request, jsonify
from utils.admin import *

admin_bp = Blueprint("admin", __name__)

@admin_bp.route("/admin/add_product", methods=["POST"])
def add_product():
    data = request.get_json()
    name = data.get("name")
    description = data.get("description")
    price = data.get("price")
    category_id = data.get("category_id")
    supplier_id = data.get("supplier_id")
    warranty_period = data.get("warranty_period")
    result = create_product(name, description, price, category_id, supplier_id, warranty_period)
    return jsonify(result)

@admin_bp.route("/admin/update_product", methods=["POST"])
def update_product_route():
    data = request.get_json()
    product_id = data.get("product_id")
    name = data.get("name")
    description = data.get("description")
    price = data.get("price")
    category_id = data.get("category_id")
    supplier_id = data.get("supplier_id")
    warranty_period = data.get("warranty_period")
    result = update_product(product_id, name, description, price, category_id, supplier_id, warranty_period)
    return jsonify(result)

@admin_bp.route("/admin/remove_product", methods=["POST"])
def remove_product_route():
    data = request.get_json()
    product_id = data.get("product_id")
    result = remove_product(product_id)
    return jsonify(result)
