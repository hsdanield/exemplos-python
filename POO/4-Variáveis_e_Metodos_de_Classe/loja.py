class Loja:

    tarifa = 1.03

    def __init__(self, endereco: str) -> None:
        self.__endereco = endereco

    def apresentar_endereco(self) -> None:
        print(self.__endereco)

    @classmethod
    def vender(cls) -> int:
        return 40 * cls.tarifa

    @classmethod
    def alterar_tarifa(cls, nova_tarifa: int) -> None:
        cls.tarifa = nova_tarifa

loja_a = Loja("Loja_A")
loja_b = Loja("Loja_B")

loja_a.apresentar_endereco() # Loja_A

print(loja_a.vender()) 
print(loja_b.vender()) 

loja_a.alterar_tarifa(1.50)

print(loja_a.vender()) 
print(loja_b.vender()) 