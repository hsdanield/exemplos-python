class MinhaClasse:

    def __init__(self, att: int):
      self.meu_atributo = "Ola Mundo"
      self.meu_atributo2 = att

    def meu_metodo(self) -> None:
        print(self.meu_atributo2)

    def meu_metodo2(self, num: int, mult: int) -> int:
        return num * mult

objeto = MinhaClasse("valor_atributo_2")
objeto.meu_metodo()
result = objeto.meu_metodo2(3, 5)
print(result)