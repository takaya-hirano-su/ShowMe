from flask import Blueprint, abort, make_response
from flask_jwt_extended import jwt_required, get_jwt_identity

from infra.settings import session

from domain.model.user_food import UserFood
from domain.model.recipe_food import RecipeFood
from domain.model.recipe import Recipe, RecipeSchema

recipes_suggestions_router = Blueprint(
    "recipes_suggestions_router", __name__, url_prefix="/recipes_suggestions"
)


@recipes_suggestions_router.route("/", methods=["GET"])
@jwt_required()
def get_recipes_suggestions():
    user_id = get_jwt_identity()
    if not user_id:
        return abort(403)

    s = session()
    try:
        user_food_ids = [
            user_food.food_id
            for user_food in s.query(UserFood).filter(UserFood.user_id == user_id).all()
        ]
        recipe_ids = [
            recipe_food.recipe_id
            for recipe_food in s.query(RecipeFood)
            .filter(RecipeFood.food_id.in_(user_food_ids))
            .distinct(RecipeFood.recipe_id)
            .all()
        ]
        recipes = s.query(Recipe).filter(Recipe.id.in_(recipe_ids), Recipe.is_public==True).all()
    except Exception as e:
        s.rollback()
        print(e)
        abort(500)
    finally:
        s.close()

    return make_response({"recipes":RecipeSchema(many=True).dump(recipes)}, 200)
