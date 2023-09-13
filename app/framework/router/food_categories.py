from flask import Blueprint,Response,jsonify
from uuid import UUID

from infra.settings import engine
from sqlalchemy.orm import sessionmaker

from domain.model.food_categories import FoodCategory

def is_uuid(s,version=4):
    try:
        uuid_obj = UUID(s, version=version)
    except ValueError:
        return False
    return str(uuid_obj) == s

food_categories_router = Blueprint('food_categories_router', __name__, url_prefix='/food_categories')

@food_categories_router.route('/', methods=['POST'])
def register_food_category():
    return 'register food_category'

@food_categories_router.route('/', methods=['GET'])
def get_food_categories():

    return jsonify({"food_categories":food_categories})

@food_categories_router.route('/<food_category_id>', methods=['GET'])
def get_food_category(food_category_id):

    SessionClass=sessionmaker(engine)
    session=SessionClass()

    try:
        food_category=session.query(FoodCategory).filter_by(id=food_category_id).one_or_none()

    except Exception as e:
        if not is_uuid(food_category_id):
            return jsonify({"error":"Bad Request"})
        
        elif food_category is None:
            return jsonify({"error":"Not found"})
        
        else:
            return jsonify({"error":"Internal Server Error"})
    
    return jsonify({"name":food_category.name})
