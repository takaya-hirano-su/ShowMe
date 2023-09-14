from domain.model.recipe import Recipe, recipe_category_schema
from flask import Blueprint, Response, abort, request
from flask_jwt_extended import get_jwt_identity, jwt_required
from infra.settings import session
from jsonschema import validate
from repository.recipes import RecipesRepository
from util.validate import is_uuid
from validate.recipes import register_recipe_schema, update_recipe_schema

recipes_router = Blueprint("recipes_router", __name__, url_prefix="/recipes")
recipes_repository = RecipesRepository(session)


@recipes_router.route("/", methods=["POST"])
@jwt_required()
def register_recipe():
    user_id = get_jwt_identity()
    if not user_id:
        return abort(403)
    if not request.is_json:
        return abort(400)
    json = request.get_json()
    try:
        validate(json, register_recipe_schema)
    except Exception as e:
        abort(400)
    user_id = get_jwt_identity()
    if not user_id:
        abort(403)

    title = json["title"]
    thumbnail_url = json["thumbnail_url"]
    recipe_category_id = json["recipe_category_id"]
    description = json["description"]
    is_public = json["is_public"]
    is_draft = json["is_draft"]
    foods = json["foods"]
    recipes_repository.create_recipe(
        user_id=user_id,
        recipe_category_id=recipe_category_id,
        title=title,
        thumbnail_url=thumbnail_url,
        description=description,
        is_public=is_public,
        is_draft=is_draft,
        foods=foods,
    )
    return Response(status=201)


@recipes_router.route("/", methods=["GET"])
def get_recipes():
    recipes = recipes_repository.get_all_recipes()
    return Response(
        response=recipe_category_schema.dumps(recipes, many=True),
        status=200,
        mimetype="application/json",
    )


@recipes_router.route("/<recipe_id>", methods=["GET"])
def get_recipe(recipe_id):
    if not is_uuid(recipe_id):
        return abort(400)
    recipe = recipes_repository.get_recipe(recipe_id)
    return Response(
        response=recipe_category_schema.dumps(recipe),
        status=200,
        mimetype="application/json",
    )


@recipes_router.route("/<recipe_id>", methods=["PUT"])
@jwt_required()
def update_recipe(recipe_id):
    user_id = get_jwt_identity()
    if not user_id:
        return abort(403)
    if not is_uuid(recipe_id):
        return abort(400)
    if not request.is_json:
        return abort(400)
    json = request.get_json()
    try:
        validate(json, update_recipe_schema)
    except Exception as e:
        return abort(400)
    title = json["title"]
    thumbnail_url = json["thumbnail_url"]
    recipe_category_id = json["recipe_category_id"]
    description = json["description"]
    is_public = json["is_public"]
    recipes_repository.update_recipe(
        user_id=user_id,
        recipe_id=recipe_id,
        recipe_category_id=recipe_category_id,
        title=title,
        thumbnail_url=thumbnail_url,
        description=description,
        is_public=is_public,
    )
    return Response(status=204)


@recipes_router.route("/<recipe_id>", methods=["DELETE"])
@jwt_required()
def delete_recipe(recipe_id):
    user_id = get_jwt_identity()
    if not user_id:
        return abort(403)
    if not is_uuid(recipe_id):
        return abort(400)
    recipes_repository.delete_recipe(recipe_id, user_id)
    return Response(status=204)
