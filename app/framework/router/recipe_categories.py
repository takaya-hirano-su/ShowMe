from flask import Blueprint, request, make_response, abort
from uuid import UUID
from flask_jwt_extended import jwt_required

from infra.settings import engine
from sqlalchemy.orm import sessionmaker

from domain.model.recipe_category import RecipeCategory

recipe_categories_router = Blueprint(
    "recipe_categories_router", __name__, url_prefix="/recipe_categories"
)

def is_uuid(s, version=4):
    try:
        uuid_obj = UUID(s, version=version)
    except ValueError:
        return False
    return str(uuid_obj) == s


@recipe_categories_router.route("/", methods=["POST"])
@jwt_required()
def register_recipe_categories():
    SessionClass = sessionmaker(engine)
    session = SessionClass()

    json = request.get_json()
    recipe_category_name = json["name"]

    try:
        is_recipe_category_name = (
            session.query(RecipeCategory)
            .filter(RecipeCategory.name == recipe_category_name)
            .limit(1)
            .one_or_none()
        )
        session.add(RecipeCategory(name=recipe_category_name))
        session.commit()

    except Exception as e:
        if not is_recipe_category_name is None:
            abort(403)
        else:
            abort(400)

    return make_response({"success": "OK"}, 201)


@recipe_categories_router.route("/", methods=["GET"])
def get_recipe_categories():
    SessionClass = sessionmaker(engine)
    session = SessionClass()

    try:
        recipe_categories = []
        for recipe_category in session.query(RecipeCategory).all():
            recipe_categories.append({"id": recipe_category.id, "name": recipe_category.name})

    except Exception as e:
        abort(500)

    return make_response({"food_categories": recipe_category}, 200)


@recipe_categories_router.route("/<recipe_categories_id>", methods=["GET"])
def get_recipe_category(recipe_categories_id):
    SessionClass = sessionmaker(engine)
    session = SessionClass()

    try:
        recipe_category = (
            session.query(RecipeCategory).filter_by(id=recipe_categories_id).one_or_none()
        )

    except Exception as e:
        if not is_uuid(recipe_categories_id):
            abort(400)

        elif recipe_category is None:
            abort(404)
        else:
            abort(500)

    return make_response({"name": recipe_category.name}, 200)


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