from flask import Blueprint, Response, abort, jsonify, request
from flask_jwt_extended import get_jwt_identity, jwt_required
from jsonschema import validate

from infra.settings import session
from repository.users_foods import UsersFoodsRepository
from validate.users_foods import register_user_food_schema, update_user_food_schema

users_foods_router = Blueprint("users_foods_router", __name__, url_prefix="/foods")
users_foods_repository = UsersFoodsRepository(session)


@users_foods_router.route("/", methods=["POST"])
@jwt_required()
def add_user_foods():
    if not request.json:
        abort(400)
    user_id = get_jwt_identity()
    json = request.json
    try:
        validate(json, register_user_food_schema)
    except Exception as e:
        abort(400)
    users_foods_repository.post_users_foods(
        user_id,
        json["name"],
        json["amount"],
        json["deadline"],
        json["expired_at"],
        json["food_id"],
    )
    return Response(status=201)


@users_foods_router.route("/", methods=["GET"])
@jwt_required()
def get_user_foods():
    user_id = get_jwt_identity()
    if not user_id:
        abort(403)
    ufs = users_foods_repository.get_users_foods(user_id)
    response = []
    for uf in ufs:
        response.append(
            {
                "id": uf.id,
                "user_id": uf.user_id,
                "name": uf.name,
                "amount": uf.amount,
                "deadline": uf.deadline,
                "expired_at": uf.expired_at,
                "food_id": uf.food_id,
            }
        )
    return jsonify(response)


@users_foods_router.route("/<food_id>", methods=["PUT"])
@jwt_required()
def update_user_food(food_id):
    user_id = get_jwt_identity()
    if not user_id:
        abort(403)
    if not request.json:
        abort(400)
    json = request.json
    try:
        validate(json, update_user_food_schema)
    except Exception as e:
        abort(400)

    users_foods_repository.put_users_food(
        user_id,
        food_id,
        json["name"],
        json["amount"],
        json["deadline"],
        json["expired_at"],
        json["food_id"],
    )
    return Response(status=204)


@users_foods_router.route("/<food_id>", methods=["DELETE"])
@jwt_required()
def delete_user_food(food_id):
    user_id = get_jwt_identity()
    if not user_id:
        abort(403)
    users_foods_repository.delete_users_food(user_id, food_id)
    return Response(status=204)
