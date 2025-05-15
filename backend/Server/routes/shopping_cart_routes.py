from flask import Blueprint, request, jsonify

shopping_cart_bp = Blueprint("shoppingcart", __name__)

@shopping_cart_bp.route("/shoppingcart/add", methods=["POST"])
def add_to_cart():
    pass

@shopping_cart_bp.route("/shoppingcart/update", methods=["POST"])
def update_cart():
    pass

@shopping_cart_bp.route("/shoppingcart/remove", methods=["POST"])
def remove_from_cart():
    pass
