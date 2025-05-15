from flask import Blueprint, request, jsonify

payment_bp = Blueprint("payment", __name__)

@payment_bp.route("/payment/fetch", methods=["GET"])
def fetch_order():
    pass

@payment_bp.route("/payment/e_transfer", methods=["POST"])
def fetch_order():
    pass