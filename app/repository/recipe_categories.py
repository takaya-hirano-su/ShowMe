from flask import abort

from domain.model.recipe_category import RecipeCategory


class RecipeCategoriesRepository:
    def __init__(self, session):
        self.session = session

    def get_recipe_categories(self) -> list[RecipeCategory]:
        s = self.session()
        try:
            recipe_categories = s.query(RecipeCategory).all()
        except Exception:
            s.rollback()
            abort(500)
        finally:
            s.close()
        return recipe_categories

    def get_recipe_category(self, recipe_categories_id: str) -> RecipeCategory:
        s = self.session()
        try:
            recipe_category = (
                s.query(RecipeCategory)
                .filter(RecipeCategory.id == recipe_categories_id)
                .limit(1)
                .one_or_none()
            )
            if recipe_category is None:
                abort(404)
        except Exception:
            s.rollback()
            abort(500)
        finally:
            s.close()
        return recipe_category

    def register_recipe_categories(self, recipe_category: RecipeCategory):
        s = self.session()
        try:
            r = (
                s.query(RecipeCategory)
                .filter(RecipeCategory.name == recipe_category.name)
                .first()
            )
        except Exception:
            abort(500)
        if r is not None:
            abort(409)
        try:
            s.add(recipe_category)
            s.commit()
        except Exception:
            s.rollback()
            abort(500)
        finally:
            s.close()
