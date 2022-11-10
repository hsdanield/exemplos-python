from .interface import Repositorio


class MysqlRepositorio(Repositorio):

    def inserir(self, dado: any) -> None:
        print('Inserindo {} no banco MySql'.format(dado))

    def deletar(self, dado: any) -> None:
        print('Removendo {} no banco MySql'.format(dado))
