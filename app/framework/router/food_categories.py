from uuid import UUID

from flask import Blueprint, abort, make_response, request
from flask_jwt_extended import jwt_required
from sqlalchemy.orm import sessionmaker

from domain.model.food_categories import FoodCategory
from infra.settings import engine

food_categories_router = Blueprint(
    "food_categories_router", __name__, url_prefix="/food_categories"
)


def is_uuid(s, version=4):
    try:
        uuid_obj = UUID(s, version=version)
    except ValueError:
        return False
    return str(uuid_obj) == s


@food_categories_router.route("/", methods=["POST"])
@jwt_required()
def register_food_category():
    SessionClass = sessionmaker(engine)
    session = SessionClass()

    if not request.is_json:
        abort(400)
    json = request.get_json()
    food_category_name = json["name"]

    try:
        is_food_category_name = (
            session.query(FoodCategory)
            .filter(FoodCategory.name == food_category_name)
            .limit(1)
            .one_or_none()
        )
        session.add(FoodCategory(name=food_category_name))
        session.commit()

    except Exception as e:
        if not is_food_category_name is None:
            abort(403)
        else:
            abort(400)

    return make_response({"success": "OK"}, 201)


@food_categories_router.route("/", methods=["GET"])
def get_food_categories():
    SessionClass = sessionmaker(engine)
    session = SessionClass()

    try:
        food_categories = []
        for food_category in session.query(FoodCategory).all():
            food_categories.append({"id": food_category.id, "name": food_category.name})

    except Exception as e:
        abort(500)

    return make_response({"food_categories": food_categories}, 200)


@food_categories_router.route("/<food_category_id>", methods=["GET"])
def get_food_category(food_category_id):
    SessionClass = sessionmaker(engine)
    session = SessionClass()

    try:
        food_category = (
            session.query(FoodCategory).filter_by(id=food_category_id).one_or_none()
        )

    except Exception as e:
        if not is_uuid(food_category_id):
            abort(400)

        elif food_category is None:
            abort(404)
        else:
            abort(500)

    return make_response({"name": food_category.name}, 200)
