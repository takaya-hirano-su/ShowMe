from flask import Blueprint, Response, abort, request
from flask_jwt_extended import get_jwt_identity, jwt_required
from jsonschema import validate

from domain.model.dish import dish_category_schema
from infra.settings import session
from repository.dishes import DishesRepository
from util.validate import is_uuid
from validate.dishes import register_dish_schema, update_dish_schema

dishes_router = Blueprint("dishes_router", __name__, url_prefix="/dishes")
dishes_repository = DishesRepository(session)


@dishes_router.route("/", methods=["POST"])
@jwt_required()
def register_dish():
    if not request.is_json:
        abort(400)
    json = request.get_json()
    try:
        validate(json, register_dish_schema)
    except Exception as e:
        abort(400)
    user_id = get_jwt_identity()
    if not user_id:
        abort(400)
    dishes_repository.post_dish(user_id, json["recipe_id"])
    return Response(status=201)


@dishes_router.route("/", methods=["GET"])
@jwt_required()
def get_dishes():
    user_id = get_jwt_identity()
    if not user_id:
        abort(400)
    dishes = dishes_repository.get_dishes(user_id)
    return Response(
        status=200,
        response=dish_category_schema.dumps(dishes, many=True),
        mimetype="application/json",
    )


@dishes_router.route("/<dish_id>", methods=["DELETE"])
@jwt_required()
def delete_dish(dish_id):
    user_id = get_jwt_identity()
    if not user_id:
        abort(400)
    if not is_uuid(dish_id):
        abort(400)
    dishes_repository.delete_dish(dish_id, user_id)
    return Response(status=200)


@dishes_router.route("/<dish_id>", methods=["PUT"])
@jwt_required()
def update_dish(dish_id):
    if not request.is_json:
        abort(400)
    json = request.get_json()
    try:
        validate(json, update_dish_schema)
    except Exception as e:
        abort(400)
    user_id = get_jwt_identity()
    if not user_id:
        abort(400)
    if not is_uuid(dish_id):
        abort(400)
    dishes_repository.update_dish(dish_id, user_id, json["recipe_id"])
    return Response(status=200)
