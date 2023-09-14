from flask import Blueprint, Response, abort
from flask_jwt_extended import get_jwt_identity, jwt_required

from domain.model.recipe import Recipe, recipe_category_schema
from infra.settings import session
from repository.recipes import RecipesRepository
from util.validate import is_uuid

users_recipes_router = Blueprint(
    "users_recipes_router", __name__, url_prefix="/<user_id>/recipes"
)

recipes_repository = RecipesRepository(session)


@users_recipes_router.route("/", methods=["GET"])
@jwt_required()
def get_user_recipes(user_id):
    id = get_jwt_identity()
    if user_id != id:
        abort(403)
    if not is_uuid(user_id):
        abort(400)
    recipes = recipes_repository.get_users_recipes(user_id)
    return Response(
        response=recipe_category_schema.dumps(recipes, many=True),
        status=200,
        mimetype="application/json",
    )
