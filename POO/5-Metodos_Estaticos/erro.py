class Erro:
    """
        @staticmethod: Atribuimos um contexto unico e separado. 
        Muito utilizado como ESPECIFICADOR.
    """
    @staticmethod
    def error_500():
        print("Internal Server Error.")

    @staticmethod
    def error_404():
        print("Not Found.")


Erro.error_404()
Erro.error_500()