from datetime import datetime
from uuid import UUID

import bcrypt
from flask import Blueprint, abort, jsonify, make_response, request
from flask_jwt_extended import JWTManager, get_jwt_identity, jwt_required
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import sessionmaker

from domain.model.user import User
from framework.router.users_path.foods import users_foods_router
from framework.router.users_path.recipes import users_recipes_router
from infra.settings import engine

users_router = Blueprint("users_router", __name__, url_prefix="/users")
users_router.register_blueprint(users_foods_router)
users_router.register_blueprint(users_recipes_router)


@users_router.route("/", methods=["POST"])
def register_user():
    SessionClass = sessionmaker(engine)
    session = SessionClass()

    name = request.json["name"]
    icon_url = request.json["icon_url"]
    mail_address = request.json["mail_address"]
    password = request.json["password"]

    password_hash = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())

    new_user = User(
        name=name,
        icon_url=icon_url,
        mail_address=mail_address,
        password_hash=password_hash.decode("utf-8"),
    )

    try:
        session.add(new_user)
        session.commit()
    except IntegrityError:
        session.rollback()
        abort(400, description="User with the given mail address already exists.")
    except Exception as e:
        session.rollback()
        abort(400, description=str(e))

    return make_response({"success": "OK"}, 201)


@users_router.route("/", methods=["PUT"])
@jwt_required()
def update_user():
    SessionClass = sessionmaker(engine)
    session = SessionClass()

    user_id = get_jwt_identity()
    user = session.query(User).filter_by(id=user_id).first()
    if not user:
        abort(404, description="User not found.")

    data = request.json

    if "name" in data:
        user.name = data["name"]

    if "icon_url" in data:
        user.icon_url = data["icon_url"]

    if "mail_address" in data:
        user.mail_address = data["mail_address"]

    if "password" in data:
        password = bcrypt.hashpw(data["password"].encode("utf-8"))
        user.password_hash = password.decode("utf-8")

    try:
        session.commit()
    except Exception as e:
        session.rollback()
        abort(400, description=str(e))

    return make_response({"success": "OK"}, 204)


@users_router.route("/", methods=["DELETE"])
@jwt_required()
def delete_user():
    SessionClass = sessionmaker(engine)
    session = SessionClass()

    user_id = get_jwt_identity()
    user = session.query(User).filter_by(id=user_id).first()
    if not user:
        abort(404)

    user.deleted_at = datetime.utcnow()
    try:
        session.commit()
    except Exception as e:
        session.rollback()
        abort(400, description=str(e))

    return make_response({"success": "OK"}, 204)


@users_router.route("/<user_id>", methods=["GET"])
def get_user(user_id):
    SessionClass = sessionmaker(engine)
    session = SessionClass()

    user = session.query(User).filter_by(id=user_id).first()
    if user:
        return (
            jsonify(
                {
                    "id": user.id,
                    "name": user.name,
                    "icon_url": user.icon_url,
                    "created_at": user.created_at,
                    "deleted_at": user.deleted_at,
                }
            ),
            200,
        )
    else:
        abort(404)
