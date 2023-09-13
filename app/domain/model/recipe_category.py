from uuid import uuid4

from sqlalchemy import Column, DateTime, String
from sqlalchemy.dialects.postgresql import UUID

from infra.settings import Base


class RecipeCategory(Base):
    __tablename__ = "recipe_categories"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    name = Column("name", String, nullable=False)

    def __repr__(self):
        return f"<RecipeCategory(id={self.id}, name={self.name})>"


if __name__ == "__main__":
    from infra.settings import engine

    Base.metadata.create_all(bind=engine)
