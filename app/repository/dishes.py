from uuid import UUID

from flask import abort

from domain.model.dish import Dish
from domain.model.recipe import Recipe
from domain.model.user import User


class DishesRepository:
    def __init__(self, session) -> None:
        self.session = session

    def post_dish(self, user_id: UUID, recipe_id: UUID) -> None:
        s = self.session()
        try:
            u = s.query(User).filter(User.id == user_id).one()
            r = s.query(Recipe).filter(Recipe.id == recipe_id).one()
        except Exception as e:
            s.rollback()
            abort(400)
        dish = Dish(user_id=u.id, recipe_id=r.id)
        try:
            s.add(dish)
            s.commit()
        except Exception as e:
            s.rollback()
            abort(500)
        finally:
            s.close()

    def get_dishes(self, user_id) -> list:
        s = self.session()
        try:
            dishes = s.query(Dish).filter(Dish.user_id == user_id).all()
        except Exception as e:
            s.rollback()
            abort(500)
        finally:
            s.close()
        return dishes

    def delete_dish(self, dish_id: UUID, user_id: UUID) -> None:
        s = self.session()
        try:
            dish = s.query(Dish).filter(Dish.id == dish_id).one()
        except Exception as e:
            s.rollback()
            abort(400)
        if dish.user_id != user_id:
            abort(403)
        try:
            s.delete(dish)
            s.commit()
        except Exception as e:
            s.rollback()
            abort(500)
        finally:
            s.close()

    def update_dish(self, dish_id: UUID, user_id: UUID, recipe_id: UUID) -> None:
        s = self.session()
        try:
            dish = s.query(Dish).filter(Dish.id == dish_id).one()
        except Exception as e:
            s.rollback()
            abort(400)
        if dish.user_id != user_id:
            abort(403)
        try:
            s.query(Dish).filter(Dish.id == dish_id).update({"recipe_id": recipe_id})
            s.commit()
        except Exception as e:
            s.rollback()
            abort(500)
        finally:
            s.close()
