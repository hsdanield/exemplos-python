from infra.configs.connection import DBConnectionHandler
from infra.entities.state import State
from datetime import datetime


class StateRepository:
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
                data = db.session.query(State).all()
                return data
            except Exception as exception:
                db.session.rollback()
                raise exception

    def select_id(self, id_state):
        with DBConnectionHandler() as db:
            try:
                data = (
                    db.session.query(State)
                    .filter(State.id_state == id_state)
                    .one_or_none()
                )
                if data:
                    return data

                print("State with ID: {} not found".format(id_state))
                return

            except Exception as exception:
                db.session.rollback()
                raise exception

    def insert(self, state: State):
        with DBConnectionHandler() as db:
            try:
                data_insert = State(
                    ibge_code=state.ibge_code,
                    initials=state.initials,
                    name=state.name,
                    id_country=state.id_country,
                    dt_create=datetime.now(),
                    dt_update=datetime.now(),
                )

                db.session.add(data_insert)
                db.session.commit()

            except Exception as exception:
                db.session.rollback()
                raise exception

    def delete(self, id_state):
        with DBConnectionHandler() as db:
            try:
                state_del: State = (
                    db.session.query(State)
                    .filter(State.id_state == id_state)
                    .one_or_none()
                )

                if state_del:
                    db.session.delete(state_del)
                    db.session.commit()
                    print("State({}) deletado com sucesso.".format(state_del))
                    return

                print("State with ID: {} not found".format(state_del))
                return

            except Exception as exception:
                db.session.rollback()
                raise exception

    def update(self, id_state, state: State):
        with DBConnectionHandler() as db:

            try:

                state_up: State = (
                    db.session.query(State)
                    .filter(State.id_state == id_state)
                    .one_or_none()
                )
                if state_up:
                    state_up.ibge_code = state.ibge_code
                    state_up.initials = state.initials
                    state_up.name = state.name
                    state_up.id_country = state.id_country
                    state_up.dt_update = datetime.now()
                    db.session.commit()

            except Exception as exception:
                db.session.rollback()
                raise exception
