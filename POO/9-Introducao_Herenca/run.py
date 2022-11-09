class Mae:

    def __init__(self, endereco) -> None:
        self.endereco = endereco
        self.sobrenome = "Silva"

    def comer(self) -> None:
        print("Estou Comendo...")

    def estudar(self) -> None:
        print("Estou Estudando...")


class Filho(Mae):

    def __init__(self, endereco) -> None:
        super().__init__(endereco)

    def brincar(self, brinquedo) -> None:
        print(f"Estou brincando com {brinquedo}")


ana = Mae("Endereco Mae")
clara = Filho("Rua Filha")
clara.estudar()
clara.brincar("boneca")

print(clara.endereco)
