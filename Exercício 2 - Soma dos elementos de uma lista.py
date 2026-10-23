def soma_elementos(lista):
    """Devolve a soma dos números inteiros da lista."""
    soma = 0
    for numero in lista:
        soma += numero
    return soma


numeros = input("Digite números inteiros separados por espaço: ")
lista = [int(numero) for numero in numeros.split()]

print(soma_elementos(lista))