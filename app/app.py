from flask import Flask

import framework.router.dishes as dishes_router
import framework.router.food_categories as food_categories_router
import framework.router.foods as foods_router
import framework.router.recipe_categories as recipe_categories_router
import framework.router.recipes as recipes_router
import framework.router.recipes_suggestions as recipes_suggestions_router
import framework.router.users as users_router

app = Flask(__name__)

app.register_blueprint(users_router.users_router)
app.register_blueprint(food_categories_router.food_categories_router)
app.register_blueprint(foods_router.foods_router)
app.register_blueprint(dishes_router.dishes_router)
app.register_blueprint(recipe_categories_router.recipe_categories_router)
app.register_blueprint(recipes_router.recipes_router)
app.register_blueprint(recipes_suggestions_router.recipes_suggestions_router)


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/test")
def test():
    return "test"
