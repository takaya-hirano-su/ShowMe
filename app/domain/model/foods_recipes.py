from uuid import uuid4

from sqlalchemy import Column, DateTime, String
from sqlalchemy.dialects.postgresql import UUID

from infra.settings import Base


class FoodsRecipe(Base):
    __tablename__ = "foods_recipes"
    recipe_id = Column(
        "recipe_id", Integer, primary_key=True, ForeignKey("recipes.id")
    )
    food_id = Column(
        "food_id", Integer, primary_key=True, ForeignKey("foods.id")
    )
    amount = Column("amount", Integer, nullable=False)

    def __repr__(self):
        return f"<FoodsRecipe(recipe_id={self.recipe_id}, food_id={self.food_id}, amount={self.amount})>"


if __name__ == "__main__":
    from infra.settings import engine

    Base.metadata.create_all(bind=engine)
