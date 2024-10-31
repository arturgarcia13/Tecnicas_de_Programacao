import matematica

def testa_aritmetica():
    print(matematica.soma(1, 2))
    print(matematica.subtracao(2, 3))

def testa_geometria():
    print(matematica.area_circulo(1))
    print(matematica.area_retangulo(1, 2))

def testa_estatistica():
    print(matematica.media_simples([1, 2, 3]))

testa_aritmetica()
testa_geometria()
testa_estatistica()