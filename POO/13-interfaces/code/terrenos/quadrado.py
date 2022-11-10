from interfaces.formas import FormasInterface


class TerrenoQuadrado(FormasInterface):

    def __init__(self, lado: int) -> None:
        self.__lado = lado

    def get_perimetro(self) -> int:
        perimetro = self.__lado * 4
        return perimetro

    def get_area(self) -> int:
        area = self.__lado * self.__lado
        return area
