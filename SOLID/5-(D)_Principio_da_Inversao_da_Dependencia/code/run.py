from typing import Type
from db.interface import Repositorio
from db.mysql_repositorio import MysqlRepositorio
from db.mongo_repositorio import MongoRepositorio


class Usuario:

    # Injeção de dependencia
    def __init__(self, repositorio: Type[Repositorio]) -> None:
        self.__repositorio = repositorio

    def armazenar_dados(self, dado: any) -> None:
        self.__repositorio.inserir(dado)

    def remover_dados(self, dado: any) -> None:
        self.__repositorio.deletar(dado)


usuario_a = Usuario(MysqlRepositorio())
usuario_b = Usuario(MongoRepositorio())

usuario_a.armazenar_dados("dados_mysql.csv")
usuario_b.armazenar_dados("dados_mongo.csv")

