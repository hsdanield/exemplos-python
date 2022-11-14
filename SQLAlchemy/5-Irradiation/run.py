from typing import List

from sqlalchemy import create_engine

from entities.address import Address
from entities.user import User
from repositories.start_repository import create_all, drop_all, Repository

engine = create_engine("mysql+pymysql://root:root@localhost:3306/dev", echo=True, future=True)
drop_all(engine)
create_all(engine)

repository = Repository(engine)

spongebob = User(
    name="spongebob",
    fullname="Spongebob Squarepants",
    addresses=[Address(email_address="spongebob@sqlalchemy.org")]
)

sandy = User(
    name="sandy",
    fullname="Sandy Cheeks",
    addresses=[
        Address(email_address="sandy@sqlalchemy.org"),
        Address(email_address="sandy@squirrelpower.org"),
    ]
)
patrick = User(name="patrick", fullname="Patrick Star")

repository.insert_users([spongebob, sandy, patrick])

users = repository.select_users_by_names(["spongebob", "sandy"])
print(users)

addresses = repository.select_addresses()
print(addresses)

#
# # select
# session = Session(engine)
# stmt = select(User).where(User.name.in_(["spongebob", "sandy"]))
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
# stmt = select(User).where(User.name == "patrick")
# patrick = session.scalars(stmt).one()
# print(patrick)
