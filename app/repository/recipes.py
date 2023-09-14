from uuid import UUID

from flask import abort

from domain.model.food import Food
from domain.model.recipe import Recipe
from domain.model.recipe_food import RecipeFood
from domain.model.user import User


class RecipesRepository:
    def __init__(self, session) -> None:
        self.session = session

    def create_recipe(
        self,
        user_id: UUID,
        recipe_category_id: UUID,
        title: str,
        thumbnail_url: str,
        description: str,
        is_public: bool,
        is_draft: bool,
        foods: list,
    ) -> None:
        recipe = Recipe(
            user_id=user_id,
            recipe_category_id=recipe_category_id,
            title=title,
            thumbnail_url=thumbnail_url,
            description=description,
            is_public=is_public,
            is_draft=is_draft,
        )
        s = self.session()
        try:
            u = s.query(User).filter(User.id == user_id).one()
        except Exception as e:
            s.rollback()
            abort(400)

        try:
            s.add(recipe)
            s.commit() #一旦commitしないと, recipeにIDが振られない
            s.add_all(
                [
                    RecipeFood(
                        recipe_id=recipe.id,
                        food_id=food["food_id"],
                        amount=food["amount"],
                    )
                    for food in foods
                ]
            )
            s.commit()
        except Exception as e:
            s.rollback()
            abort(500)
        finally:
            s.close()

    def get_all_recipes(self) -> list:
        s = self.session()
        try:
            recipes = s.query(Recipe).filter(Recipe.is_public == True).all()
        except Exception as e:
            s.rollback()
            abort(500)
        finally:
            s.close()
        return recipes

    def get_recipe(self, recipe_id: UUID) -> Recipe:
        s = self.session()
        try:
            recipe = s.query(Recipe).filter(Recipe.id == recipe_id).one()
        except Exception as e:
            s.rollback()
            abort(500)
        finally:
            s.close()
        return recipe

    def update_recipe(
        self,
        user_id: UUID,
        recipe_id: UUID,
        title: str,
        thumbnail_url: str,
        recipe_category_id: UUID,
        description: str,
        is_public: bool,
    ) -> None:
        s = self.session()
        try:
            s.query(Recipe).filter(
                Recipe.id == recipe_id, Recipe.user_id == user_id
            ).update(
                {
                    "title": title,
                    "thumbnail_url": thumbnail_url,
                    "recipe_category_id": recipe_category_id,
                    "description": description,
                    "is_public": is_public,
                }
            )
            s.commit()
        except Exception as e:
            s.rollback()
            abort(500)
        finally:
            s.close()

    def delete_recipe(self, recipe_id: UUID, user_id: UUID) -> None:
        s = self.session()
        try:
            recipe = s.query(Recipe).filter(Recipe.id == recipe_id).one()
        except Exception as e:
            s.rollback()
            abort(400)
        if recipe.user_id != user_id:
            abort(403)
        try:
            s.delete(recipe)
            s.commit()
        except Exception as e:
            s.rollback()
            abort(500)
        finally:
            s.close()

    def get_users_recipes(self, user_id: UUID) -> list:
        s = self.session()
        try:
            recipes = s.query(Recipe).filter(Recipe.user_id == user_id).all()
        except Exception as e:
            s.rollback()
            abort(500)
        finally:
            s.close()
        return recipes
