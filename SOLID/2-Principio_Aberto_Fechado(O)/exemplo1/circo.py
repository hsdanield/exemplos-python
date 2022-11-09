# Classe Aberta para extensões
class Circo:

    def apresentar(self, apresentador: any):
        apresentador.apresentar_show()


class Malabarista:

    def apresentar_show(self):
        print("Malabarista apresentando seu show.")


class Palhaco:

    def apresentar_show(self):
        print("Palhaco apresentando seu show.")


circo = Circo()
malabarista = Malabarista()
palhaco = Palhaco()

circo.apresentar(malabarista)
circo.apresentar(palhaco)
