from uuid import uuid4

from sqlalchemy import Boolean, Column, DateTime, ForeignKey, String
from sqlalchemy.dialects.postgresql import UUID

from infra.settings import Base


class Recipe(Base):
    __tablename__ = "recipes"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    user_id = Column(
        UUID(as_uuid=True), ForeignKey("users.id"), nullable=False, default=uuid4
    )
    recipe_category_id = Column(
        UUID(as_uuid=True),
        ForeignKey("recipe_categories.id"),
        nullable=False,
        default=uuid4,
    )
    title = Column("title", String, nullable=False)
    thumbnail_url = Column("thumbnail_url", String)
    description = Column("description", String)
    is_public = Column("is_public", Boolean, nullable=False)
    is_draft = Column("is_draft", Boolean, nullable=False)
    created_at = Column("created_at", DateTime, server_default="now()")
    updated_at = Column("updated_at", DateTime)
    deleted_at = Column("deleted_at", DateTime)

    def __repr__(self):
        return f"<Recipe(id={self.id}, user_id={self.user_id}, recipe_category_id={self.recipe_category_id}, title={self.title}, thumbnail_url={self.thumbnail_url}, description={self.description}, is_public={self.is_public}, is_draft={self.is_draft}, created_at={self.created_at}, updated_at={self.updated_at}, deleted_at={self.deleted_at})>"
