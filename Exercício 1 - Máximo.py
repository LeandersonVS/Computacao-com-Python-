def maximo(numero1, numero2):
	if numero1 > numero2:
		return numero1
	return numero2


if __name__ == "__main__":
	primeiro = int(input("Digite o primeiro número: "))
	segundo = int(input("Digite o segundo número: "))
	print("O maior número é", maximo(primeiro, segundo))
