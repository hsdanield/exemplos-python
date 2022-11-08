class Calculadora:

    def __init__(self):
        self.__resultado: float = 0.0

    def calcular(self, op: str, num: float):

        if op == "+":
            self.__resultado = self.__adicionar(self.__resultado, num)
        elif op == "-":
            self.__resultado = self.__subtrair(self.__resultado, num)
        elif op == "*":
            self.__resultado = self.__multiplicar(self.__resultado, num)
        elif op == "/":
            self.__resultado = self.__dividir(self.__resultado, num)
        else:
            print("Operação Inválida.")

    def __adicionar(self, num1: float, num2: float) -> float:
        return num1 + num2

    def __subtrair(self, num1: float, num2: float) -> float:
        return num1 - num2

    def __multiplicar(self, num1: float, num2: float) -> float:
        return num1 * num2

    def __dividir(self, num1: float, num2: float) -> float:
        try:
            result = num1 / num2
            return result
        except ZeroDivisionError:
            raise Exception("O divisor deve ser maior que zero")

    def print_resultado(self):
        print(self.__resultado)


calculadora = Calculadora()


calculadora.calcular("+", 5.5)
calculadora.calcular("+", 5.5)
calculadora.calcular("*", 2) 
calculadora.calcular("/", 10)
calculadora.print_resultado()
