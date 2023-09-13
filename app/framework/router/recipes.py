from flask import Blueprint

recipes_router = Blueprint('recipes_router', __name__, url_prefix='/recipes')

@recipes_router.route('/', methods=['POST'])
def register_recipe():
    return 'register recipe'

@recipes_router.route('/', methods=['GET'])
def get_recipes():
    return 'get recipes'
  
@recipes_router.route('/<recipe_id>', methods=['GET'])
def get_recipe(recipe_id):
    return 'get recipe ' + recipe_id

@recipes_router.route('/<recipe_id>', methods=['PUT'])
def update_recipe(recipe_id):
    return 'update recipe' + recipe_id

@recipes_router.route('/<recipe_id>', methods=['DELETE'])
def delete_recipe(recipe_id):
    return 'delete recipe ' + recipe_id