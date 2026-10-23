def vogal(caractere):
	return caractere.lower() in "aeiou"


if __name__ == "__main__":
	caractere = input("Digite um caractere: ")
	print(vogal(caractere))
