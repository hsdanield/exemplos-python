from typing import Type


class Interruptor:

    def __init__(self, comodo: str):
        self.__comodo = comodo

    def acender(self) -> None:
        print(f"Ascendendo {self.__comodo}")

    def apagar(self) -> None:
        print(f"Apagando {self.__comodo}")


class Pessoa:

    def __init__(self, nome: str):
      self.__nome = nome

    def acender_luz(self, interruptor: Type[Interruptor]):
        interruptor.acender()

    def apagar_luz(self, interruptor: Type[Interruptor]):
        interruptor.apagar()

    def dormir(self):
        print(f"{self.__nome} foi dormir...")


daniel = Pessoa("Daniel")
interruptor_quarto = Interruptor("Quarto")
interruptor_cozinha = Interruptor("Cozinha")

daniel.acender_luz(interruptor_cozinha)
daniel.acender_luz(interruptor_quarto)
daniel.apagar_luz(interruptor_quarto)
daniel.dormir()
