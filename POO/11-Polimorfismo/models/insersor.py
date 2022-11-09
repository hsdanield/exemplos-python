from typing import Dict, Type
from models.repositorio import Repositorio


class Insersor:

    def __init__(self, repositorio: Type[Repositorio]) -> None:
        self.__repo = repositorio

    def inserir_dado(self, nome: str, idade: int) -> Dict:
        registro = self.__repo.select(nome)

        if registro:
            raise Exception('O Registro ja existe...')

        novo_registro = self.__repo.insert(nome, idade)
        return novo_registro
