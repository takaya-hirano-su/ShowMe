from flask import Blueprint
from flask_jwt_extended import jwt_required

recipes_suggestions_router = Blueprint(
    "recipes_suggestions_router", __name__, url_prefix="/recipes_suggestions"
)


@recipes_suggestions_router.route("/", methods=["GET"])
@jwt_required()
def get_recipes_suggestions():
    return "get recipes_suggestions"
