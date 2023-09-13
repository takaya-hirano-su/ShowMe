from datetime import timedelta

from flask import Flask
from flask_jwt_extended import JWTManager, get_jwt_identity, jwt_required

import framework.router.dishes as dishes_router
import framework.router.food_categories as food_categories_router
import framework.router.foods as foods_router
import framework.router.login as login_router
import framework.router.recipe_categories as recipe_categories_router
import framework.router.recipes as recipes_router
import framework.router.recipes_suggestions as recipes_suggestions_router
import framework.router.users as users_router

app = Flask(__name__)

app.config["JWT_SECRET_KEY"] = "secret"  # 暗号化に使用するキー
app.config["JWT_ALGORITHM"] = "HS256"  # 暗号化署名のアルゴリズム
app.config["JWT_LEEWAY"] = 0  # 有効期限に対する余裕時間
app.config["JWT_EXPIRATION_DELTA"] = timedelta(seconds=300)  # トークンの有効期間
app.config["JWT_NOT_BEFORE_DELTA"] = timedelta(seconds=0)  # トークンの使用を開始する相対時間

jwt = JWTManager(app)

app.register_blueprint(users_router.users_router)
app.register_blueprint(food_categories_router.food_categories_router)
app.register_blueprint(foods_router.foods_router)
app.register_blueprint(dishes_router.dishes_router)
app.register_blueprint(recipe_categories_router.recipe_categories_router)
app.register_blueprint(recipes_router.recipes_router)
app.register_blueprint(recipes_suggestions_router.recipes_suggestions_router)
app.register_blueprint(login_router.login_router)


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/test")
@jwt_required()
def test():
    user_id = get_jwt_identity()
    print(user_id)
    return "test"
