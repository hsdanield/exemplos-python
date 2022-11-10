from interface import AveVoadora
from interface import AveQueNaoVoa


class Canario(AveVoadora):

    def comer(self):
        print("Estou comendo!")

    def voar(self):
        print("Estou voando!")

    def gritar(self):
        print("Estou gritando!")


class Pinguim(AveQueNaoVoa):

    def comer(self):
        print("Estou comendo!")

    def gritar(self):
        print("Estou gritando!")
