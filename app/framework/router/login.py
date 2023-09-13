from dataclasses import dataclass

from flask import Blueprint, jsonify, request
from flask_jwt_extended import create_access_token
from jsonschema import validate

from domain.model.user import User
from infra.settings import session

login_router = Blueprint("login", __name__, url_prefix="/login")

login_json_schema = {
    "type": "object",
    "properties": {
        "mail_address": {"type": "string"},
        "password": {"type": "string"},
    },
    "required": ["mail_address", "password"],
}


@login_router.route("/", methods=["POST"])
def login():
    if request.json is None:
        return jsonify({"message": "JSON形式でリクエストしてください。"}), 400
    json = request.get_json()
    try:
        validate(json, login_json_schema)
    except Exception:
        return jsonify({"message": "JSON形式が不正です。"}), 400

    email = json["mail_address"]
    password = json["password"]

    try:
        user = session.query(User).filter(User.mail_address == email).first()
    except Exception:
        return jsonify({"message": "internal server error"}), 500

    if user is None:
        return jsonify({"message": "emailかpasswordが間違っています。"}), 400
    if not user.verify_password(password):
        return jsonify({"message": "emailかpasswordが間違っています。"}), 400

    access_token = create_access_token(identity=user.id)
    response = jsonify({"access_token": access_token})
    return response, 200
