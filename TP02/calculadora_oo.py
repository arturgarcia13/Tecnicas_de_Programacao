class Calculadora:
    def __init__(self):
        self.__acumulador = 0.0
        

    def somar(self, operando_a: int, operando_b = None):
        if operando_b == None:
            self.__acumulador += operando_a
            return self.__acumulador
        self.__acumulador = operando_a + operando_b
        return operando_a + operando_b

    def subtrair(self, operando_a, operando_b = None):
        if operando_b == None:
            self.__acumulador -= operando_a
            return self.__acumulador
        self.__acumulador = operando_a - operando_b
        return operando_a - operando_b

    def multiplicar(self, operando_a, operando_b = None):
        if operando_b == None:
            self.__acumulador = operando_a * self.__acumulador
            return self.__acumulador
        self.__acumulador = operando_a * operando_b 
        return operando_a * operando_b

    def dividir(self, operando_a, operando_b = None):
        if operando_b == 0:
            raise ValueError("Divisão por zero não é permitida.")
        if operando_b == None:
            self.__acumulador = operando_a / self.__acumulador
            return self.__acumulador
        self.__acumulador = operando_a / operando_b
        return operando_a / operando_b
    def get_acumulador(self):
        return self.__acumulador