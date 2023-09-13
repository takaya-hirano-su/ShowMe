from flask import Blueprint

users_recipes_router = Blueprint('users_recipes_router', __name__, url_prefix='/<user_id>/recipes')

@users_recipes_router.route('/', methods=['GET'])
def get_user_recipes(user_id):
    return 'get user recipes ' + user_id
  