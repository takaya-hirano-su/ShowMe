from flask import Blueprint, jsonify, request
from uuid import UUID

from infra.settings import engine
from sqlalchemy.orm import sessionmaker

from domain.model.food_categories import FoodCategory

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
def register_food_category():
    SessionClass = sessionmaker(engine)
    session = SessionClass()

    food_category_name = request.form["name"]

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
            return jsonify(
                {
                    "error": f"Forbidden. food_category '{food_category_name}' already exists."
                }
            )
        else:
            return jsonify({"error": "Bad Request"})

    return jsonify({"success": 200})


@food_categories_router.route("/", methods=["GET"])
def get_food_categories():
    SessionClass = sessionmaker(engine)
    session = SessionClass()

    try:
        food_categories = []
        for food_category in session.query(FoodCategory).all():
            food_categories.append({"id": food_category.id, "name": food_category.name})
    except Exception as e:
        return jsonify({"error": "Internal Server Error"})

    return jsonify({"food_categories": food_categories})


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
            return jsonify({"error": "Bad Request"})

        elif food_category is None:
            return jsonify({"error": "Not found"})

        else:
            return jsonify({"error": "Internal Server Error"})

    return jsonify({"name": food_category.name})
