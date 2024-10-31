acumulador = 0.0

def soma(operando_a=None, operando_b=None):
    if operando_b == None:
        memoria(acumulador + operando_a)
        return acumulador
    memoria(operando_a + operando_b)
    return acumulador

def subtracao(operando_a=None, operando_b=None):
    if operando_b == None:
        memoria(acumulador - operando_a)
        return acumulador
    memoria(operando_a - operando_b)
    return acumulador

def multiplicacao(operando_a=None, operando_b=None):
    if operando_b == None:
        memoria(acumulador * operando_a)
        return acumulador
    memoria(operando_a * operando_b)
    return acumulador

def divisao(operando_a=None, operando_b=None):
    if operando_b == None:
        memoria(acumulador / operando_a)
        return acumulador
    memoria(operando_a / operando_b)
    return acumulador

def memoria(resultado):
    global acumulador
    acumulador = resultado

def clean():
    global acumulador
    acumulador = 0

