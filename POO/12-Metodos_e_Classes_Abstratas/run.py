from abs_class import AbstractClass


class Filho(AbstractClass):

    def apresentar_metodo(self) -> None:
        print(self.atributo)

    def metodo_abstrato(self) -> None:
        print('Implementando metodo abstrato')


filho = Filho()
filho.apresentar_metodo()
filho.metodo('Estou aqui.')
filho.metodo_abstrato()


# Error: não pode instanciar classe
# abstractClass = AbstractClass()
# abstractClass.metodo('Fazendo algo.')
