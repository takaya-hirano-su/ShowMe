from flask import Blueprint, request, make_response, abort
from uuid import UUID
from flask_jwt_extended import jwt_required
from datetime import datetime

from infra.settings import session

from domain.model.food import Food

foods_router = Blueprint("foods_router", __name__, url_prefix="/foods")


def is_uuid(s, version=4):
    try:
        uuid_obj = UUID(s, version=version)
    except ValueError:
        return False
    return str(uuid_obj) == s


@foods_router.route("/", methods=["POST"])
@jwt_required()
def register_food():
    return "register food"


@foods_router.route("/", methods=["GET"])
def get_foods():

    test_food=Food(
        name="にんじん",
        icon_url="https://media.delishkitchen.tv/article/1100/eco9bggfutt.jpeg?version=1636508482",
        food_category_id="7efa9f06-6907-4215-b05a-386c1c4d3077",
        deadline=datetime.now()
    )
    session.add(test_food)
    session.commit()

    try:
        foods=[]
        for food in session.query(Food).all():
            foods.append({
                "id":food.id,
                "name":food.name,
                "icon_url":food.icon_url,
                "food_category_id":food.food_category_id,
                "deadline":food.deadline,
            })

    except Exception as e:
        session.rollback()
        abort(500)

    finally:
        session.query(Food).delete()
        session.commit()
        session.close()

    return make_response({"foods":foods},200)


@foods_router.route("/<food_id>", methods=["GET"])
def get_food(food_id):
    return "get food " + food_id

@foods_router.errorhandler(400)
def bad_request(error):
    return make_response({"error": "Bad Request"}, 400)


@foods_router.errorhandler(403)
def forbidden(error):
    return make_response({"error": "Forbidden"}, 403)


@foods_router.errorhandler(404)
def not_found(error):
    return make_response({"error": "Not found"}, 404)


@foods_router.errorhandler(500)
def internal_server_error(error):
    return make_response({"error": "Internal Server Error"}, 500)