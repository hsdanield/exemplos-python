from typing import List

from infra.repository.state_repository import StateRepository
from infra.repository.country_repository import CountryRepository
from infra.entities.state import State


state_repository = StateRepository()
country_repository = CountryRepository()

data_state = state_repository.select_all()
data_country = country_repository.select_all()

print(data_country)
print()

# state_repository.insert(state=State(
#     ibge_code = 111,
#     initials="DC",
#     name="Washington",
#     id_country=2
# ))

# SELECT BY ID
# print("select_id")
# br = state_repository.select_id(1)
# print(br)

# SELECT ALL
# print("select_all")
# data = state_repository.select_all()
# print(data)


# # UPDATE
# print("update")
# repo_country.update(
#     id_country=10, country=Country(initials="EU", name="Estados Unidos da América")
# )

# # SELECT ALL
# print("select_all")
# data = repo_country.select_all()
# print(data)

# # DELETE
# print("delete")
# repo_country.delete(10)
