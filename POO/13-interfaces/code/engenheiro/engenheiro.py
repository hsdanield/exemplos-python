from typing import Type
from interfaces.formas import FormasInterface


class Engenheiro:

    def __init__(self, nome) -> None:
        self.nome = nome

    def medir_perimetro(self, terreno: Type[FormasInterface]):
        perimetro = terreno.get_perimetro()
        print("{} mediu o perimetro: {} m".format(self.nome, perimetro))

    def medir_area(self, terreno: Type[FormasInterface]):
        area = terreno.get_area()
        print("{} mediu o area: {} m2".format(self.nome, area))
