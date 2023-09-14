from flask import Blueprint
from flask_jwt_extended import jwt_required

recipe_categories_router = Blueprint(
    "recipe_categories_router", __name__, url_prefix="/recipe_categories"
)


@recipe_categories_router.route("/", methods=["POST"])
@jwt_required()
def register_recipe_categories():
    return "register recipe_categories"


@recipe_categories_router.route("/", methods=["GET"])
def get_recipe_categories():
    return "get recipe_categories"


@recipe_categories_router.route("/<recipe_categories_id>", methods=["GET"])
def get_recipe_category(recipe_categories_id):
    return "get recipe_category " + recipe_categories_id