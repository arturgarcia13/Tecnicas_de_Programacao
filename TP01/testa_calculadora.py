import calculadora as calc

def teste1(operando_a,operando_b):
    soma_a_b = calc.soma(operando_a,operando_b)
    print(f'A soma de {operando_a} e {operando_b} é {soma_a_b}')
    subtracao_a_b = calc.subtracao(operando_a,operando_b)
    print(f'A subtração de {operando_a} e {operando_b} é {subtracao_a_b}')
    multiplicacao_a_b = calc.multiplicacao(operando_a,operando_b)
    print(f'A multiplicação de {operando_a} e {operando_b} é {multiplicacao_a_b}')
    divisao_a_b = calc.divisao(operando_a,operando_b)
    print(f'A divisão de {operando_a} e {operando_b} é {divisao_a_b}')

def teste_memoria2():
    soma_1 = calc.soma(2,3)
    print(f'A soma de 2 e 3 é {soma_1}')
    soma_2 = calc.soma(3)
    print(f'A soma de {soma_1} e 3 é {soma_2}')
    soma_3 = calc.soma(5)
    print(f'A soma de {soma_2} e 5 é {soma_3}')
    calc.clean()
    
    sub_1 = calc.subtracao(2,3)
    print(f'A subtração de 2 e 3 é {sub_1}')
    sub_2 = calc.subtracao(3)
    print(f'A subtração de {sub_1} e 3 é {sub_2}')
    sub_3 = calc.subtracao(5)
    print(f'A subtração de {sub_2} e 5 é {sub_3}')
    calc.clean()
    
    mult_1 = calc.multiplicacao(2,3)
    print(f'A multiplicação de 2 e 3 é {mult_1}')
    mult_2 = calc.multiplicacao(3)
    print(f'A multiplicação de {mult_1} e 3 é {mult_2}')
    mult_3 = calc.multiplicacao(5)
    print(f'A multiplicação de {mult_2} e 5 é {mult_3}')
    calc.clean()
    
    div_1 = calc.divisao(300,10)
    print(f'A divisão de 300 e 10 é {div_1}')
    div_2 = calc.divisao(3)
    print(f'A divisão de {div_1} e 3 é {div_2}')
    div_3 = calc.divisao(5)
    print(f'A divisão de {div_2} e 5 é {div_3}')
    calc.clean()

teste_memoria2()