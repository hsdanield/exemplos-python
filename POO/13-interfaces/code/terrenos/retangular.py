from interfaces.formas import FormasInterface


class TerrenoRetangular(FormasInterface):

    def __init__(self, comprimento: int, largura: int) -> None:
        self.__comprimento = comprimento
        self.__largura = largura

    def get_perimetro(self) -> int:
        perimetro = (self.__comprimento * 2) + (self.__largura * 2)
        return perimetro

    def get_area(self) -> int:
        area = self.__comprimento * self.__largura
        return area
