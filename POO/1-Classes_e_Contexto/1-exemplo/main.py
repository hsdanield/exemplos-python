from pessoa import Pessoa
from datetime import datetime

p1 = Pessoa(nome="Daniel", idade=25)

p1.andar(25)
p1.andar(25)


p1.parar_andar()
p1.parar_andar()

p1.ligar("Ze Gotinha")
p1.ligar("Ze pilintra")

p1.desligar()
p1.desligar()

p1.ligar("Ze pilintra")

p1.get_data_nascimento()