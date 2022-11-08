class CadastroMultiResponsabilidade:

    def cadastrar(self, nome: str, idade: str) -> None:
        if isinstance(nome, str) and isinstance(idade, int):  # Responsabilidade de verificação
            print("Acessando banco de dados.")  # Responsabilidade cadastro
            print(f"Cadastrar o Usuario {nome}, Idade {idade}.")
        else:
            print("Dados inválidos.")  # Responsabilidade de indicar erro


class CadastroSRP:

    def cadastrar(self, nome: str, idade: str) -> None:
        if self.__verificar_dados(nome, idade):
            self.__armazenar_usuario(nome, idade)
        else:
            self.__indicar_erro()

    def __verificar_dados(self, nome: str, idade: int) -> bool:
        if isinstance(nome, str) and isinstance(idade, int):
            return True

        return False

    def __armazenar_usuario(self, nome: str, idade: int) -> None:
        print("Acessando banco de dados.")
        print(f"Cadastrar o Usuario {nome}, Idade {idade}.")

    def __indicar_erro(self):
        print("Dados inválidos.")


if __name__ == "__main__":
    cadastro = CadastroSRP()
    # Tentando cadastrar com idade tipo str
    cadastro.cadastrar("Daniel", "25")

    # Cadastrando
    cadastro.cadastrar("Daniel", 25)
