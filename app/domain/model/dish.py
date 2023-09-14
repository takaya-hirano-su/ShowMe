from uuid import uuid4

from sqlalchemy import Column, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID

from app import ma
from infra.settings import Base


class Dish(Base):
    __tablename__ = "dishes"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    user_id = Column(
        UUID(as_uuid=True), ForeignKey("users.id"), nullable=False, default=uuid4
    )
    recipe_id = Column(
        UUID(as_uuid=True), ForeignKey("recipes.id"), nullable=False, default=uuid4
    )
    created_at = Column("created_at", DateTime, server_default="now()")

    def __repr__(self):
        return f"<Dish(id={self.id}, user_id={self.user_id}, recipe_id={self.recipe_id}, created_at={self.created_at})>"


class DishCategorySchema(ma.Schema):
    class Meta:
        fields = ("id", "user_id", "recipe_id", "created_at")


dish_category_schema = DishCategorySchema()

if __name__ == "__main__":
    from infra.settings import engine

    Base.metadata.create_all(bind=engine)
