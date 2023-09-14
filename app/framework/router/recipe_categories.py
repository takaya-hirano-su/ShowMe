from flask import Blueprint, Response, abort, jsonify, request
from flask_jwt_extended import jwt_required
from jsonschema import validate

from domain.model.recipe_category import RecipeCategory, RecipeCategorySchema
from infra.settings import session
from repository.recipe_categories import RecipeCategoriesRepository
from util.validate import is_uuid
from validate.recipe_categories import register_recipe_categories_schema

recipe_categories_router = Blueprint(
    "recipe_categories_router", __name__, url_prefix="/recipe_categories"
)

recipe_categories_repository = RecipeCategoriesRepository(session)


@recipe_categories_router.route("/", methods=["POST"])
@jwt_required()
def register_recipe_categories():
    if not request.is_json:
        abort(400)
    json = request.get_json()
    try:
        validate(json, register_recipe_categories_schema)
    except Exception:
        abort(400)

    name = json["name"]
    recipe_category = RecipeCategory(name=name)
    recipe_categories_repository.register_recipe_categories(recipe_category)
    return Response(status=201)


@recipe_categories_router.route("/", methods=["GET"])
def get_recipe_categories():
    recipe_categories = recipe_categories_repository.get_recipe_categories()
    print(recipe_categories)
    return Response(
        status=200,
        response=RecipeCategorySchema().dumps(recipe_categories, many=True),
        content_type="application/json",
    )


@recipe_categories_router.route("/<recipe_categories_id>", methods=["GET"])
def get_recipe_category(recipe_categories_id):
    if not is_uuid(recipe_categories_id):
        abort(400)

    recipe_category = recipe_categories_repository.get_recipe_category(
        recipe_categories_id
    )
    return Response(
        status=200,
        response=RecipeCategorySchema().dumps(recipe_category),
        content_type="application/json",
    )
