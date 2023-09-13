from flask import Blueprint
from flask_jwt_extended import jwt_required

dishes_router = Blueprint("dishes_router", __name__, url_prefix="/dishes")


@dishes_router.route("/", methods=["POST"])
@jwt_required()
def register_dish():
    return "register dish"


@dishes_router.route("/", methods=["GET"])
@jwt_required()
def get_dishes():
    return "get dishes"


@dishes_router.route("/<dish_id>", methods=["DELETE"])
@jwt_required()
def delete_dish(dish_id):
    return "delete dish " + dish_id


@dishes_router.route("/<dish_id>", methods=["PUT"])
@jwt_required()
def update_dish(dish_id):
    return "update dish" + dish_id
