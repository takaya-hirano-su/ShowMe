from flask import Blueprint

foods_router = Blueprint('foods_router', __name__, url_prefix='/foods')

@foods_router.route('/', methods=['POST'])
def register_food():
    return 'register food'
  
@foods_router.route('/', methods=['GET'])
def get_foods():
    return 'get foods'

@foods_router.route('/<food_id>', methods=['DELETE'])
def get_food(food_id):
    return 'get food ' + food_id