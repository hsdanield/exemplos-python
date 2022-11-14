from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from base import Base


class User(Base):
    __tablename__ = "user"

    id_user = Column("id_user", Integer, primary_key=True)
    name = Column("name", String(30))
    fullname = Column("fullname", String(200))
    addresses = relationship(
        "Address", back_populates="user", cascade="all, delete-orphan"
        # , lazy="joined"
    )

    def __repr__(self):
        return f"User(id_user={self.id_user!r}, name={self.name!r}," \
               f" fullname={self.fullname!r}," \
               # f" addresses={self.addresses!r}) "
