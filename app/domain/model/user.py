# Table users {
#   id uuid [pk]
#   name varchar
#   icon_url varchar
#   mail_address varchar
#   password_hash varchar
#   created_at timestamp
#   deleted_at timestamp
# }
from uuid import uuid4

from sqlalchemy import Column, DateTime, String
from sqlalchemy.dialects.postgresql import UUID

from infra.settings import Base


class User(Base):
    __tablename__ = "users"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    name = Column("name", String, nullable=False)
    icon_url = Column("icon_url", String)
    mail_address = Column("mail_address", String, unique=True, nullable=False)
    password_hash = Column("password_hash", String, nullable=False)
    created_at = Column("created_at", DateTime, server_default="now()")
    deleted_at = Column("deleted_at", DateTime)

    def __repr__(self):
        return f"<User(id={self.id}, name={self.name}, icon_url={self.icon_url}, mail_address={self.mail_address}, password_hash={self.password_hash}, created_at={self.created_at}, deleted_at={self.deleted_at})>"


if __name__ == "__main__":
    from infra.settings import engine

    Base.metadata.create_all(bind=engine)
