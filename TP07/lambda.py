# 1.1 Soma com Lambda
soma = lambda x, y: x + y
print(soma(1, 3))  # Output: 4

# 1.2 Verificar se é Par com Lambda
par = lambda x: True if x % 2 == 0 else False
print(par(2))  # Output: True

# 1.3 Quadrados dos números de 0 a 9 com map e lambda
lista = list(map(lambda x: x**2, range(10)))
print(lista)  # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# 1.4 Converter Celsius para Fahrenheit com função composta
celsius_to_farenheit = lambda c: (c * 9/5) + 32
round_value = lambda x: round(x)
funcao_composta = lambda c: round_value(celsius_to_farenheit(c))
lista_celsius = [10, 100, 0, 30]
celsius_convertidos = list(map(
        lambda c: funcao_composta(c), 
        lista_celsius
    ))
print(celsius_convertidos)  # Output: [50, 212, 32, 86]

# 2.1 Transformar palavras em maiúsculas
uppercase = [
    palavra for palavra in map(
        lambda x: x.upper(), 
        ["python", "lambda", "map"]
    )
]
print(uppercase)  # Output: ['PYTHON', 'LAMBDA', 'MAP']

# 2.2 Quadrados dos números usando expressões geradoras
lista_quadrados = [
    num for num in map(
        lambda x: x**2, 
        range(10)
    )
]
print(lista_quadrados)  # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# 2.3 Contar palavras e caracteres em frases
frases = ["Python é incrível", "Lambda são úteis", "Map é funcional"]
resultados = [
    info for info in map(lambda frase: {
        "palavras": len(frase.split()), 
        "caracteres": len(frase)
    }, frases)
]
print(resultados)
# Output: [{'palavras': 3, 'caracteres': 16}, {'palavras': 3, 'caracteres': 14}, {'palavras': 3, 'caracteres': 14}]

# 3.1 Filtrar números positivos
lista_numeros = [-10, 15, -20, 25, 0, 30]
numeros_positivo = [
    num for num in filter(
        lambda x: x > 0, 
        lista_numeros
    )
]
print(numeros_positivo)  # Output: [15, 25, 30]

# 3.2 Filtrar palavras com mais de 5 caracteres
palavras = ['Python', 'é', 'incrível', 'Lambda', 'são', 'úteis', 'Map', 'é', 'funcional']
palavras_filtradas = [
    palavra for palavra in filter(
        lambda palavra: len(palavra) > 5, 
        palavras
    )
]
print(palavras_filtradas)  # Output: ['Python', 'incrível', 'Lambda', 'funcional']

# 3.3 Filtrar números divisíveis por 3 ou 5 e positivos
numeros_aleatorios = [-84, -87, -61, 42, -26, -16, 81, -72, -67, -14, -3, 91, 30, -94, 35, -23, 94, 18, -11, 48]
num_filtrado = [
    num for num in filter(
        lambda x: (x % 3 == 0 or x % 5 == 0) and x > 0, 
        numeros_aleatorios
    )
]
print(num_filtrado)  # Output: [42, 81, 30, 35, 18, 48]

# 4.1 Produto de uma lista
from functools import reduce
lista_produto = [95, 18, 53, 61, 1, 42, 72, 69, 78, 57]
produto_lista = reduce(
    lambda x, y: x * y, 
    lista_produto
)
print(produto_lista)  # Output: 361411725404320

# 4.2 Maior número em uma lista
lista_maior = [95, 18, 53, 61, 1, 42, 72, 69, 78, 57]
maior_lista = reduce(
    lambda x, y: x if x >= y else y, 
    lista_maior
)
print(maior_lista)  # Output: 95

# 4.3 Converter lista de tuplas para dicionário somando valores
lista_tuplas = [("a", 1), ("b", 2), ("a", 3)]
tupla_to_dict = reduce(
    lambda acc, tupla: acc.update({tupla[0]: acc.get(tupla[0], 0) + tupla[1]}) or acc,
    lista_tuplas,
    {}
)
print(tupla_to_dict)  # Output: {'a': 4, 'b': 2}

# 5.1 Números pares entre 1 e 50
pares = [
    num for num in filter(
        lambda x: x % 2 == 0, range(1, 51)
    )
]
for n in pares:
    print(n)  # Output: 2, 4, 6, ..., 50 (números pares)

# 5.2 Soma dos quadrados de números de 1 a 10
soma_quadrados = reduce(
    lambda x, y: x + y, 
    [num**2 for num in range(1, 11)]
)
print(soma_quadrados)  # Output: 385

# 5.3 Primeiros 10 números da sequência de Fibonacci
def fibonacci():
    a, b = 0, 1
    while True:
        yield b
        a, b = b, a + b

fib = fibonacci()
fibo_10 = [next(fib) for _ in range(10)]
print(fibo_10)  # Output: [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

# 5.4 Gerar números primos em um intervalo
def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

ger_primos = [
    num for num in filter(
        lambda x: is_prime(x), 
        range(10, 20)  # Exemplo: intervalo de 10 a 20
    )
]
print(ger_primos)  # Output: [11, 13, 17, 19]

# 5.5 Fibonacci até um valor limite
def fibonacci(limit):
    a, b = 0, 1
    while b <= limit:
        yield b
        a, b = b, a + b

fib_list = [val for val in fibonacci(int(input("Qual o valor limite? ")))]
print(fib_list)
