from uuid import uuid4

from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.dialects.postgresql import UUID

from infra.settings import Base


class FoodsRecipe(Base):
    __tablename__ = "foods_recipes"
    recipe_id = Column(
        UUID(as_uuid=True), ForeignKey("recipes.id"), primary_key=True, default=uuid4
    )
    food_id = Column(
        UUID(as_uuid=True), ForeignKey("foods.id"), primary_key=True, default=uuid4
    )
    amount = Column("amount", Integer, nullable=False)

    def __repr__(self):
        return f"<FoodsRecipe(recipe_id={self.recipe_id}, food_id={self.food_id}, amount={self.amount})>"
