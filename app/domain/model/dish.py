from uuid import uuid4

from sqlalchemy import Column, ForeignKey, DateTime
from sqlalchemy.dialects.postgresql import UUID

from infra.settings import Base


class Dish(Base):
    __tablename__ = "dishes"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    user_id = Column(UUID(as_uuid=True),ForeignKey('user.id'), nullable=False, default=uuid4)
    recipe_id = Column(UUID(as_uuid=True), ForeignKey('recipe.id'), nullable=False, default=uuid4)
    created_at = Column("created_at", DateTime, server_default="now()")

    def __repr__(self):
        return f"<Dish(id={self.id}, user_id={self.user_id}, recipe_id={self.recipe_id}, created_at={self.created_at})>"


if __name__ == "__main__":
    from infra.settings import engine

    Base.metadata.create_all(bind=engine)
