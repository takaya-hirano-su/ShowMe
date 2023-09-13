from uuid import uuid4

from sqlalchemy import Column, DateTime, String
from sqlalchemy.dialects.postgresql import UUID

from infra.settings import Base


class Food_categories(Base):
    __tablename__ = "users"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    name = Column("name", String, nullable=False)

    def __repr__(self):
        return f"<Food_categories(id={self.id}, name={self.name})>"


if __name__ == "__main__":
    from infra.settings import engine

    Base.metadata.create_all(bind=engine)
