from flask import Blueprint
from flask_jwt_extended import jwt_required

food_categories_router = Blueprint(
    "food_categories_router", __name__, url_prefix="/food_categories"
)


@food_categories_router.route("/", methods=["POST"])
@jwt_required()
def register_food_category():
    return "register food_category"


@food_categories_router.route("/", methods=["GET"])
def get_food_categories():
    return "get food_categories"


@food_categories_router.route("/<food_category_id>", methods=["GET"])
def get_food_category(food_category_id):
    return "get food_category " + food_category_id
