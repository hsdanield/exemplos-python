from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from base import Base


class Address(Base):
    __tablename__ = "address"

    id_address = Column("id_address", Integer, primary_key=True)
    email_address = Column("email_address", String(100), nullable=False)
    user_id = Column("user_id", Integer, ForeignKey("user.id_user"), nullable=False)
    user = relationship(
        "User", back_populates="addresses", lazy="subquery"
    )

    def __repr__(self):
        return f"Address(id_address={self.id_address!r}, email_address={self.email_address!r}, user={self.user})"
