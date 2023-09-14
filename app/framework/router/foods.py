from flask import Blueprint, abort, make_response, request
from flask_jwt_extended import get_jwt_identity, jwt_required
from jsonschema import validate

from domain.model.food import FoodSchema
from infra.settings import session
from repository.foods import FoodRepository
from util.validate import is_uuid
from validate.foods import register_food_schema

foods_router = Blueprint("foods_router", __name__, url_prefix="/foods")
food_repository = FoodRepository(session)


@foods_router.route("/", methods=["POST"])
@jwt_required()
def register_food():
    if not request.is_json:
        abort(401)

    json = request.get_json()

    try:
        validate(json, register_food_schema)
    except Exception as e:
        abort(400)

    user_id = get_jwt_identity()
    if not user_id:
        abort(400)

    food_repository.post_food(
        json["name"], json["icon_url"], json["food_category_id"], json["deadline"]
    )

    return make_response({"success": "OK"}, 201)


@foods_router.route("/", methods=["GET"])
def get_foods():
    foods = food_repository.get_foods()

    return make_response({"foods": FoodSchema(many=True).dump(foods)}, 200)


@foods_router.route("/<food_id>", methods=["GET"])
def get_food(food_id):
    if not is_uuid(food_id):
        abort(400)

    food = food_repository.get_food(food_id)

    return make_response(FoodSchema(many=False).dump(food), 200)
