from flask import Blueprint

recipes_suggestions_router = Blueprint('recipes_suggestions_router', __name__, url_prefix='/recipes_suggestions')

@recipes_suggestions_router.route('/', methods=['GET'])
def get_recipes_suggestions():
    return 'get recipes_suggestions'
  