from datetime import datetime
from uuid import UUID

from flask import abort
from sqlalchemy.orm import Session, scoped_session

from domain.model.food import Food
from domain.model.food_categories import FoodCategory


class FoodRepository:
    def __init__(self, session: scoped_session) -> None:
        self.session = session

    def post_food(
        self, name: str, icon_url: str, food_category_id: UUID, deadline: datetime
    ) -> None:
        s: Session = self.session()
        try:
            food_category = (
                s.query(FoodCategory)
                .filter(FoodCategory.id == food_category_id)
                .one_or_none()
            )
        except Exception as e:
            s.rollback()
            abort(400)

        if food_category is None:
            abort(400)

        food = Food(
            name=name,
            icon_url=icon_url,
            food_category_id=food_category_id,
            deadline=deadline,
        )
        try:
            s.add(food)
            s.commit()
        except Exception as e:
            s.rollback()
            abort(500)
        finally:
            s.close()

    def get_foods(self) -> list:
        s: Session = self.session()
        try:
            foods = s.query(Food).all()
        except Exception as e:
            s.rollback()
            abort(500)
        finally:
            s.close()

        return foods

    def get_food(self, food_id: UUID) -> Food:
        s: Session = self.session()
        try:
            food = s.query(Food).filter(Food.id == food_id).one_or_none()
        except Exception as e:
            s.rollback()
            abort(500)
        finally:
            s.close()

        if food is None:
            abort(404)

        return food
