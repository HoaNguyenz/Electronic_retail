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
    # Add email and name to response if registration is successful
    if "message" in response:
        response["email"] = data["email"]
        response["name"] = f"{data['first_name']} {data['last_name']}"
    return jsonify(response)

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.json
    if not data or "email" not in data or "password" not in data:
        return jsonify({"error": "Invalid input"}), 400
    response = authenticate_user(data["email"], data["password"])
    # Add email and name to response if login is successful
    if response.get("message") == "Login successful":
        response["email"] = data["email"]
        # Optionally, fetch user name from DB in authenticate_user and return it
        if "name" not in response:
            response["name"] = ""  # You can enhance this to fetch the name
    return jsonify(response)