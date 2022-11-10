from typing import Type, List
from produtos import Produto


class CarrinhoDeCompras:

    def __init__(self) -> None:
        self.__produtos: List[Type[Produto]] = []

    def adicionar_produto(self, produto: Type[Produto]) -> None:
        self.__produtos.append(produto)

    def finalizar_compra(self) -> None:
        print('Compras Finalizadas!')

        for produto in self.__produtos:
            produto.informacoes_produto()

        self.__produtos = []
