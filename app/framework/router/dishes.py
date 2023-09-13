from flask import Blueprint

dishes_router = Blueprint('dishes_router', __name__, url_prefix='/dishes')

@dishes_router.route('/', methods=['POST'])
def register_dish():
    return 'register dish'

@dishes_router.route('/', methods=['GET'])
def get_dishes():
    return 'get dishes'
  
@dishes_router.route('/<dish_id>', methods=['DELETE'])
def delete_dish(dish_id):
    return 'delete dish ' + dish_id

@dishes_router.route('/<dish_id>', methods=['PUT'])
def update_dish(dish_id):
    return 'update dish' + dish_id