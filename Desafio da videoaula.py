from math import sqrt

a = float(input())
b = float(input())
c = float(input())

delta = b ** 2 - 4 * a * c

if delta < 0:
	print("esta equação não possui raízes reais")
elif delta == 0:
	raiz = -b / (2 * a)
	print("a raiz desta equação é", raiz)
else:
	raiz1 = (-b - sqrt(delta)) / (2 * a)
	raiz2 = (-b + sqrt(delta)) / (2 * a)
	menor = min(raiz1, raiz2)
	maior = max(raiz1, raiz2)
	print("as raízes da equação são", menor, "e", maior)
