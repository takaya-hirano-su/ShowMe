from flask import Blueprint
from flask_jwt_extended import jwt_required

users_foods_router = Blueprint("users_foods_router", __name__, url_prefix="/foods")


@users_foods_router.route("/", methods=["POST"])
@jwt_required()
def add_user_foods():
    return "add user foods"


@users_foods_router.route("/", methods=["GET"])
@jwt_required()
def get_user_foods():
    return "get user foods"


@users_foods_router.route("/<food_id>", methods=["PUT"])
@jwt_required()
def update_user_food(food_id):
    return "update user food " + food_id


@users_foods_router.route("/<food_id>", methods=["DELETE"])
@jwt_required()
def delete_user_food(food_id):
    return "delete user food " + food_id
