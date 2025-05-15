from flask import Blueprint, request, jsonify

order_bp = Blueprint("order", __name__)

@order_bp.route("/order/fetch", methods=["GET"])
def fetch_order():
    pass
@order_bp.route("/order/checkout", methods=["POST"])
def place_order():
    pass

@order_bp.route("/order/cancel", methods=["POST"])
def cancel_order():
    pass
