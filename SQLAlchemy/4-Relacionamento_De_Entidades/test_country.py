from typing import List

from infra.repository.country_repository import CountryRepository
from infra.entities.country import Country


repo_country = CountryRepository()

# SELECT ALL
print("select_all")
data = repo_country.select_all()
print(data)

# INSERT
print()
new_country = Country(initials="EUA", name="Estados Unidos")
repo_country.insert(new_country)

# SELECT BY ID
print("select_id")
eua = repo_country.select_id(1)
print(eua)

# UPDATE
print("update")
repo_country.update(
    id_country=10, country=Country(initials="EU", name="Estados Unidos da América")
)

# SELECT ALL
print("select_all")
data = repo_country.select_all()
print(data)

# DELETE
print("delete")
repo_country.delete(10)
