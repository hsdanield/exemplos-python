from infra.configs.connection import DBConnectionHandler
from infra.entities.country import Country
from datetime import datetime


class CountryRepository:
    # def select(self):
    #     with DBConnectionHandler() as db:
    #         data = (
    #             db.session.query(Cidades)
    #             .join(Estados, Cidades.id_estado == Estados.id_estado)
    #             .with_entities(Cidades.nome, Estados.nome, Estados.sigla)
    #             .all()
    #         )
    #         return data
    def select_all(self):
        with DBConnectionHandler() as db:
            try:
                data = db.session.query(Country).all()
                return data
            except Exception as exception:
                db.session.rollback()
                raise exception

    # LIMIT: total_page TAMANHO DA PAGINA
    # OFFSET: numero da pagina
    def select_by_page(self, page, page_size):
        with DBConnectionHandler() as db:
            try:
                data = (
                    db.session.query(Country)
                    .limit(page_size)
                    .offset(page_size * page)
                    .all()
                )
                return data
            except Exception as exception:
                db.session.rollback()
                raise exception

    def select_id(self, id_country):
        with DBConnectionHandler() as db:
            try:
                data = (
                    db.session.query(Country)
                    .filter(Country.id_country == id_country)
                    .one_or_none()
                )
                if data:
                    return data

                print("Country with ID: {} not found".format(id_country))
                return

            except Exception as exception:
                db.session.rollback()
                raise exception

    def insert(self, country: Country):
        with DBConnectionHandler() as db:
            try:
                data_insert = Country(
                    initials=country.initials,
                    name=country.name,
                    dt_create=datetime.now(),
                    dt_update=datetime.now(),
                )

                db.session.add(data_insert)
                db.session.commit()

            except Exception as exception:
                db.session.rollback()
                raise exception

    def delete(self, id_country):
        with DBConnectionHandler() as db:
            try:
                country_del: Country = (
                    db.session.query(Country)
                    .filter(Country.id_country == id_country)
                    .one_or_none()
                )

                if country_del:
                    db.session.delete(country_del)
                    db.session.commit()
                    print("Country({}) deletado com sucesso.".format(country_del))
                    return

                print("Country with ID: {} not found".format(id_country))
                return

            except Exception as exception:
                db.session.rollback()
                raise exception

    def update(self, id_country, country: Country):
        with DBConnectionHandler() as db:

            try:

                country_up: Country = (
                    db.session.query(Country)
                    .filter(Country.id_country == id_country)
                    .one_or_none()
                )
                if country_up:
                    country_up.initials = country.initials
                    country_up.name = country.name
                    country_up.dt_update = datetime.now()
                    db.session.commit()

            except Exception as exception:
                db.session.rollback()
                raise exception
