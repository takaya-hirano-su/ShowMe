from uuid import uuid4

from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.dialects.postgresql import UUID

from app import ma
from infra.settings import Base


class Food(Base):
    __tablename__ = "foods"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    name = Column("name", String, nullable=False)
    icon_url = Column("icon_url", String)
    food_category_id = Column(
        UUID(as_uuid=True),
        ForeignKey("food_categories.id"),
        nullable=False,
        default=uuid4,
    )
    deadline = Column("deadline", DateTime, nullable=False)

    def __repr__(self):
        return f"<Food(id={self.id}, name={self.name}, icon_url={self.icon_url}, food_category_id={self.food_category_id}, deadline={self.deadline})>"


class FoodSchema(ma.Schema):
    class Meta:
        fields = ("id", "name", "icon_url", "food_category_id", "deadline")


if __name__ == "__main__":
    from infra.settings import engine

    Base.metadata.create_all(bind=engine)
