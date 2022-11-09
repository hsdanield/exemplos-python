from modulos import Casa, Pessoa

casa_amigo = Casa()
daniel = Pessoa("Daniel")

daniel.set_local(casa_amigo)
casa_amigo.set_proprietario(daniel)

proprietario = casa_amigo.get_proprietario()
proprietario.se_apresentar()

daniel.apresentar_local()
