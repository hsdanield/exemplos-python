class Produto:

    def __init__(self, nome: str, valor: int) -> None:
        self.__nome = nome
        self.__valor = valor

    def informacoes_produto(self) -> None:
        print('Produto: {} / Valor: R$ {},00'.format(self.__nome, self.__valor))
