from calculadora_oo import Calculadora

def teste_simples():
    calc = Calculadora()  # Instância da classe

    print(f"Soma de 10 + 5: {calc.somar(10, 5)}")
    print(f"Subtração de 10 - 5: {calc.subtrair(10, 5)}")
    print(f"Multiplicação de 10 * 5: {calc.multiplicar(10, 5)}")
    print(f"Divisão de 10 % 5: {calc.dividir(10, 5)}")

def teste_memoria():
    calc = Calculadora()

    print(f"Acumulador: {calc.get_acumulador()}")
    print(f"Soma de 10 + 5: {calc.somar(10, 5)}")
    print(f"Acumulador: {calc.get_acumulador()}")
    print(f"Soma de {calc.get_acumulador()} + 5: {calc.somar(5)}")
    print(f"Acumulador: {calc.get_acumulador()}")
    print(f"Subtração de 10 - 5: {calc.subtrair(10, 5)}")
    print(f"Acumulador: {calc.get_acumulador()}")
    print(f"Subtração de {calc.get_acumulador()} - 2: {calc.subtrair(2)}")
    print(f"Acumulador: {calc.get_acumulador()}")
    print(f"Multiplicação de 10 * 5: {calc.multiplicar(10,5)}")
    print(f"Acumulador: {calc.get_acumulador()}")
    print(f"Multiplicação de {calc.get_acumulador()} * 2: {calc.multiplicar(2)}")
    print(f"Acumulador: {calc.get_acumulador()}")
    print(f"Divisão de 100 // 5: {calc.dividir(100, 5)}")
    print(f"Acumulador: {calc.get_acumulador()}")
    print(f"Divisão de {calc.get_acumulador()} // 2: {calc.dividir(2)}")
    print(f"Acumulador: {calc.get_acumulador()}")

if __name__ == "__main__":
    teste_memoria()
