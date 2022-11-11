from infra.configs.connection import DBConnectionHandler
from infra.entities.livros import Livros


class LivrosRepository:
    def select(self):
        with DBConnectionHandler() as db:
            data = db.session.query(Livros).all()
            return data

    def insert(self, autor, titulo, genero, ano):
        with DBConnectionHandler() as db:
            data_insert = Livros(autor=autor, titulo=titulo, genero=genero, ano=ano)
            db.session.add(data_insert)
            db.session.commit()

    def delete(self, titulo):
        with DBConnectionHandler() as db:
            db.session.query(Livros).filter(Livros.titulo == titulo).delete()
            db.session.commit()

    def update(self, autor, titulo, genero, ano):
        with DBConnectionHandler() as db:
            db.session.query(Livros).filter(Livros.titulo == titulo).update(
                {"autor": autor, "genero": genero, "ano": ano}
            )
            db.session.commit()
