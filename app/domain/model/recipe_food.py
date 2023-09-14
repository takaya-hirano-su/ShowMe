from uuid import uuid4

from sqlalchemy import Boolean, Column, DateTime, ForeignKey, String
from sqlalchemy.dialects.postgresql import UUID

from infra.settings import Base


class RecipeFood(Base):
    __tablename__ = "recipe_foods"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    recipe_id = Column(
        UUID(as_uuid=True),
        ForeignKey("recipes.id", ondelete="CASCADE"),
        nullable=False,
        default=uuid4,
    )
    food_id = Column(
        UUID(as_uuid=True), ForeignKey("foods.id"), nullable=False, default=uuid4
    )
    amount = Column("amount", String, nullable=False)
    created_at = Column("created_at", DateTime, server_default="now()")

    def __repr__(self):
        return f"<Recipe(id={self.id}, user_id={self.user_id}, recipe_category_id={self.recipe_category_id}, title={self.title}, thumbnail_url={self.thumbnail_url}, description={self.description}, is_public={self.is_public}, is_draft={self.is_draft}, created_at={self.created_at}, updated_at={self.updated_at}, deleted_at={self.deleted_at})>"
