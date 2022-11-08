class Pessoa:

    def __init__(self, nome, idade, cpf):
        self.nome = nome
        self.idade = idade
        self.__cpf = cpf

    def correr(self):
        print(f"{self.nome} está correndo.")

    def beber(self, bebida):
        if bebida in ["cerveja", "vodka"]:
            print("Apresente o documento")
            self.__apresentar_documento

        print(f"{self.nome} está Bebendo {bebida}.")

    def __apresentar_documento(self):
        print(self.__cpf)


daniel = Pessoa("Daniel", 25, "31289037128")
print(daniel.nome)
print(daniel.idade)

daniel.correr()

daniel.beber("água")
daniel.beber("cerveja")

