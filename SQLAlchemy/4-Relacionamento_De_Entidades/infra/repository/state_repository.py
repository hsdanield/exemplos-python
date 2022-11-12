from infra.configs.connection import DBConnectionHandler
from infra.entities.state import State
from sqlalchemy.orm.exc import NoResultFound


class StateRepository:
    def select(self):
        with DBConnectionHandler() as db:
            try:
                data = db.session.query(State).all()
                return data
            except Exception as exception:
                db.session.rollback()
                raise exception

    def insert(self, state: State):
        with DBConnectionHandler() as db:
            try:
                data_insert = State(
                    initials=state.initials,
                    name=state.name,
                    dt_create=state.dt_create,
                    dt_update=state.dt_update,
                )

                db.session.add(data_insert)
                db.session.commit()

            except Exception as exception:
                raise exception

    def delete(self, id_estado):
        with DBConnectionHandler() as db:
            db.session.query(State).filter(State.id_estado == id_estado).delete()
            db.session.commit()

    def update(self, id_estado, codigo_ibge, sigla, nome):
        with DBConnectionHandler() as db:
            db.session.query(State).filter(State.id_estado == id_estado).update(
                {"codigo_ibge": codigo_ibge, "sigla": sigla, "nome": nome}
            )
            db.session.commit()
