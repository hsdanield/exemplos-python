class MinhaClasse:
    """
        Quando uma variável Estática é declarada, então uma unica copia
        da variável é criada e compartilhada e com todos objetos a nível 
        de classe. São um "tipo de variável global da classe"
    """

    estatico = "Valor Estático"  # Variável Estática

    def __init__(self, estado: bool) -> None:
        self.estado = estado

    def print_estatico(self):
        print(self.estatico)

    # Caso algum objeto chamar esse Metodo todas as variaveis estatico seram alteradas
    @classmethod
    def mudar_estatico(cls):
        cls.estatico = "Valor Estático Alterado"


if __name__ == "__main__":
    obj1 = MinhaClasse(True)
    obj2 = MinhaClasse(False)

    obj1.mudar_estatico()

    obj1.print_estatico()  # Imprime: Valor Estático
    obj2.print_estatico()  # Imprime: Valor Estático Alterado
