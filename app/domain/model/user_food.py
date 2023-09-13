from uuid import uuid4

from sqlalchemy import Column, DateTime, String, Integer, ForeignKey, Float
from sqlalchemy.dialects.postgresql import UUID

from infra.settings import Base


class UserFood(Base):
    __tablename__ = "user_foods"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    name = Column("name", String, nullable=False)
    user_id = Column(
        UUID(as_uuid=True),
        Integer,
        ForeignKey("user.id"),
        nullable=False,
        default=uuid4,
    )
    food_id = Column(
        UUID(as_uuid=True),
        Integer,
        ForeignKey("food.id"),
        nullable=False,
        default=uuid4,
    )
    amount = Column("amount", Float, server_default=0.0, comment="単位無し. 数量のみ")
    deadline = Column("deadline", DateTime)
    created_at = Column("created_at", DateTime, server_default="now()")
    deleted_at = Column("deleted_at", DateTime)
    expired_at = Column("expired_at", DateTime)
    updated_at = Column("updated_at", DateTime)

    def __repr__(self):
        return f"<UserFood(id={self.id}, name={self.name}, amount={self.amount}, deadline={self.deadline}, created_at={self.created_at}, deleted_at={self.deleted_at},expired_at={self.expired_at},updated_at={self.updated_at})>"


if __name__ == "__main__":
    from infra.settings import engine

    Base.metadata.create_all(bind=engine)
