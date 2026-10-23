n = int(input("Digite o valor de n: "))

fatorial = 1
for numero in range(1, n + 1):
	fatorial *= numero

print(fatorial)
