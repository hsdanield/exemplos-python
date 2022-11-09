class MysqlDB:

    def __init__(self) -> None:
        self.__conexao = "Mysql"

    def conectar(self):
        print("Conectando ao banco Mysql...")
        return self.__conexao

    def desconectar(self) -> str:
        print("Desconectando ao banco Mysql...")

