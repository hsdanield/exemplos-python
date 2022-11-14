from typing import List

from base import Base
from entities.user import User
from entities.address import Address

from sqlalchemy import select
from sqlalchemy.orm import Session

def create_all(engine):
    Base.metadata.create_all(engine)

def drop_all(engine):
    Base.metadata.drop_all(engine)


class Repository:

    def __init__(self, engine):
        self.__engine = engine
        self.__session = Session(engine)

    # Persist entities -- Insert
    def insert_users(self, users: List[User]):
        with self.__session as db:
            db.add_all(users)
            db.commit()

    def select_users_by_names(self, names: List[str]):
        with self.__session as db:
            stmt = select(User).where(User.name.in_(["spongebob", "sandy"]))
            return self.__session.scalars(stmt).all()

    def select_addresses(self):
        with self.__session as db:
            stmt = select(Address)
            return self.__session.scalars(stmt).all()

    # def select_users_by_names(self, names: List[str]):
    #     with self.__session as db:
    #         stmt = select(User).where(User.name.in_(["spongebob", "sandy"]))
    #         return self.__session.scalars(stmt).all()

    # for user in session.scalars(stmt):
    #     print(user)
    #
    # stmt = (
    #     select(Address)
    #     .join(Address.user)
    #     .where(User.name == "sandy")
    #     .where(Address.email_address == "sandy@sqlalchemy.org")
    # )
    # sandy_address = session.scalars(stmt).one()
    #
