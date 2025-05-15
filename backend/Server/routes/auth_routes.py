from flask import Blueprint, request, jsonify
from utils.auth import register_user, authenticate_user

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.json
    required_fields = ["first_name", "last_name", "email", "phone", "address", "city", "state", "zip_code", "password", "user_type"]
    if not data or not all(field in data for field in required_fields):
        return jsonify({"error": "Invalid input"}), 400
    response = register_user(
        data["first_name"],
        data["last_name"],
        data["email"],
        data["phone"],
        data["address"],
        data["city"],
        data["state"],
        data["zip_code"],
        data["password"],
        data["user_type"]
    )
    return jsonify(response)

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.json
    if not data or "email" not in data or "password" not in data:
        return jsonify({"error": "Invalid input"}), 400
    response = authenticate_user(data["email"], data["password"])
    return jsonify(response)