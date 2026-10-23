# Bhaskara

import math

def calcular_delta(a, b, c):
    return b**2 - 4*a*c

def ler_numeros():
    a = float(input("a: "))
    b = float(input("b: "))
    c = float(input("c: "))
    return a, b, c

def imprimir_raizes(a, b, c):
    delta = calcular_delta(a, b, c)  # calculado uma só vez
    if delta > 0:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        print(f"Duas raízes: {x1} e {x2}")
    elif delta == 0:
        x = -b / (2*a)
        print(f"Uma raiz: {x}")
    else:
        print("Não há raízes reais")

a, b, c = ler_numeros()
imprimir_raizes(a, b, c)