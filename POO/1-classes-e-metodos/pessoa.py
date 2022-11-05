from datetime import datetime

class Pessoa:

    destino = None
    ano_atual = int(datetime.now().strftime("%Y"))

    # Construtor Padrão
    def __init__(self, nome, idade, andando=False, ligacao=False):
        self.nome = nome
        self.idade = idade
        self.andando = andando
        self.ligacao = ligacao
    
    
    def ligar(self, destino):
        
        if self.ligacao:
            print(f"{self.nome} ja esta em uma ligação com {self.destino}")
            return

        self.destino = destino
        self.ligacao = True
        print(f"{self.nome} entrou em uma ligação {self.destino}.")
        

    def desligar(self):
        if self.ligacao:
            print(f"{self.nome} desligou o celular.")
            self.ligacao = False
            return 
        
        print(f"{self.nome} já esta com o celular desligado.")
        



    def andar(self, velocidade):

        if self.andando:
            print(f"{self.nome} já esta andando.")
            return 

        print(f"{self.nome} está andando, velocidade {velocidade} km/h.")
        self.andando = True

    def parar_andar(self):
        if self.andando:
            self.andando = False
            print(f"{self.nome} parou de andar.")
            return 

        print(f"{self.nome} não está andando.")

    def get_data_nascimento(self):
        data_nascimento = self.ano_atual - self.idade
        print(f"{self.nome}, seu ano de nascimento é: {data_nascimento}") 
        

