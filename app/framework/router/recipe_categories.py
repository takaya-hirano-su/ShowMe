from flask import Blueprint, make_response
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


@recipe_categories_router.errorhandler(400)
def bad_request(error):
    return make_response({"error": "Bad Request"}, 400)


@recipe_categories_router.errorhandler(403)
def forbidden(error):
    return make_response({"error": "Forbidden"}, 403)


@recipe_categories_router.errorhandler(404)
def not_found(error):
    return make_response({"error": "Not Found"}, 404)


@recipe_categories_router.errorhandler(500)
def internal_server_error(error):
    return make_response({"error": "Internal Server Error"}, 500)