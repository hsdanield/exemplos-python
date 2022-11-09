from typing import Type


class Animal:

    def comer(self):
        print("O Animal está Comendo.")

    def dormir(self):
        print("O Animal esta Dormindo.")

    def andar(self):
        print("O Animal está Andando")


class Lobos(Animal):

    def __init__(self) -> None:
        super().__init__()

    def uivar(self):
        print("A lobo está uivando.")


class Aves(Animal):

    def __init__(self) -> None:
        super().__init__()

    def cantar(self):
        print("A ave está cantando.")


class Pinguim(Aves):

    def __init__(self) -> None:
        super().__init__()

    def escorregar():
        print("O pinguim está escorregando no gelo.")


class Falcao(Aves):

    def __init__(self) -> None:
        super().__init__()

    def voar():
        print("O falcão está voando.")

class Pessoa:

    def observar(self, animal: Type[Animal]):
        animal.cantar()

daniel = Pessoa()
pinguim = Aves()
daniel.observar(pinguim)