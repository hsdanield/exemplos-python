from produtos import Produto
from carrinho_de_compras import CarrinhoDeCompras

carrinho_de_compras = CarrinhoDeCompras()

#Produtos
monitor = Produto('Monitor', 1000)
cerveja = Produto('Cerveja', 5)
tv = Produto('TV', 3000)

#Adicionando Produtos ao Carrinho de Compras
carrinho_de_compras.adicionar_produto(monitor)
carrinho_de_compras.adicionar_produto(cerveja)
carrinho_de_compras.adicionar_produto(tv)

#Finalizando compra e imprimindo produtos do Carrinho de Compras
carrinho_de_compras.finalizar_compra()

