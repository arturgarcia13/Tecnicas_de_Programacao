def divisao_inteligente(func):
    def wrapper(x,y):
        print(f'Dividindo: {x}/{y}')
        if y == 0.0:
            return 'ERRO_DIV_POR_ZERO'
        return func(x,y)
    return wrapper

@divisao_inteligente
def dividir(operando_a: float, operando_b: float) -> None:
    return operando_a / operando_b

if __name__ == "__main__":
    print("--> Resultado: {}\n".format(dividir(3,3)))
    print("--> Resultado: {}\n".format(dividir(3,0)))