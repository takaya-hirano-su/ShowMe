from uuid import UUID

from flask import abort

from domain.model.user_food import UserFood


class UsersFoodsRepository:
    def __init__(self, session) -> None:
        self.session = session

    def post_users_foods(self, user_id, name, amount, deadline, expired_at, food_id):
        s = self.session()
        try:
            uf = UserFood(
                name=name,
                user_id=user_id,
                amount=amount,
                deadline=deadline,
                expired_at=expired_at,
                food_id=food_id,
            )
            s.add(uf)
            s.commit()
        except Exception as e:
            print(e)
            s.rollback()
            abort(500)
        finally:
            s.close()

    def get_users_foods(self, user_id) -> list[UserFood]:
        s = self.session()
        try:
            ufs = s.query(UserFood).filter(UserFood.user_id == user_id).all()
        except Exception as e:
            s.rollback()
            abort(500)
        finally:
            s.close()
        return ufs

    def get_users_food(self, user_id, user_food_id) -> UserFood:
        s = self.session()
        try:
            uf = s.query(UserFood).filter(UserFood.id == user_food_id).one()
        except Exception as e:
            s.rollback()
            abort(500)
        finally:
            s.close()
        if str(uf.user_id) != str(user_id):
            abort(403)
        return uf

    def put_users_food(
        self, user_id, user_food_id, name, amount, deadline, expired_at, food_id
    ) -> None:
        s = self.session()
        try:
            uf = s.query(UserFood).filter(UserFood.id == user_food_id).one()
        except Exception as e:
            s.rollback()
            abort(500)
        if str(uf.user_id) != str(user_id):
            abort(403)
        uf.name = name if name is not None else uf.name
        uf.amount = amount if amount is not None else uf.amount
        uf.deadline = deadline if deadline is not None else uf.deadline
        uf.expired_at = expired_at if expired_at is not None else uf.expired_at
        uf.food_id = food_id if food_id is not None else uf.food_id
        try:
            s.commit()
        except Exception as e:
            s.rollback()
            abort(500)
        finally:
            s.close()

    def delete_users_food(self, user_id, user_food_id) -> None:
        s = self.session()
        try:
            uf = s.query(UserFood).filter(UserFood.id == user_food_id).one()
        except Exception as e:
            s.rollback()
            abort(500)
        if str(uf.user_id) != str(user_id):
            abort(403)
        try:
            s.delete(uf)
            s.commit()
        except Exception as e:
            s.rollback()
            abort(500)
        finally:
            s.close()
