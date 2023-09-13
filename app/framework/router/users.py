from flask import Blueprint

from framework.router.users_path.foods import users_foods_router
from framework.router.users_path.recipes import users_recipes_router

users_router = Blueprint('users_router', __name__, url_prefix='/users')
users_router.register_blueprint(users_foods_router)
users_router.register_blueprint(users_recipes_router)

@users_router.route('/', methods=['POST'])
def register_user():
    return 'register user'

@users_router.route('/', methods=['PUT'])
def update_user():
    return 'update user'

@users_router.route('/', methods=['DELETE'])
def delete_user():
    return 'delete user'

@users_router.route('/<user_id>', methods=['GET'])
def get_user(user_id):
    return 'get user ' + user_id



