def maior_primo(numero):
	candidato = numero
	while candidato >= 2:
		primo = True
		divisor = 2
		while divisor * divisor <= candidato:
			if candidato % divisor == 0:
				primo = False
				break
			divisor += 1
		if primo:
			return candidato
		candidato -= 1


if __name__ == "__main__":
	valor = int(input("Digite um número inteiro maior ou igual a 2: "))
	print(maior_primo(valor))
