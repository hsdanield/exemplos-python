from typing import Type


class Conexao:

    def conectar(self):
        print("Connectando ao banco de dados")

    def desconectar(self):
        print("Desconectando ao banco de dados")


class MySQLRepo(Conexao):

    def __init__(self) -> None:
        super().__init__()

    def select(self):
        self.conectar()
        print("SELECT * FROM table")


class CasoDeUso:

    def buscar(self, db_repo: Type[MySQLRepo]):
        db_repo.select()
