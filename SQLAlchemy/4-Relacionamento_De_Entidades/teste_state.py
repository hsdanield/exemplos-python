from typing import List

from infra.repository.state_repository import StateRepository
from infra.repository.country_repository import CountryRepository
from infra.entities.state import State


class Resp:
    def get_response(self, data):
        return {"data": data}


state_repository = StateRepository()
country_repository = CountryRepository()

# data_state = state_repository.select_all()

page = 1
page_size = 50

page = page - 1

state_page1 = state_repository.select_by_page(page=page, page_size=page_size)
country_page1 = country_repository.select_by_page(page=page, page_size=page_size)

state_join_country = state_repository.select_join_country()

# print(state_page1)

print(state_join_country)
# print("-" * 50)
# print(country_page1)
