from uuid import uuid4

from sqlalchemy import Column, DateTime, String,ForeignKey,Integer
from sqlalchemy.dialects.postgresql import UUID

from infra.settings import Base


class Food(Base):
    __tablename__ = "foods"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    name = Column("name", String, nullable=False)
    icon_url = Column("icon_url", String)
    food_category_id=Column("food_category_id",Integer,ForeignKey("food_category.id"))
    deadline=Column("deadline", DateTime)


    def __repr__(self):
        return f"<User(id={self.id}, name={self.name}, icon_url={self.icon_url}, mail_address={self.mail_address}, password_hash={self.password_hash}, created_at={self.created_at}, deleted_at={self.deleted_at})>"


if __name__ == "__main__":
    from infra.settings import engine

    Base.metadata.create_all(bind=engine)
