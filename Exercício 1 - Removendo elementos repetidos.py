def remove_repetidos(lista):
    """Retorna os números da lista sem repetições, em ordem crescente."""
    return sorted(set(lista))


numeros = input("Digite números inteiros separados por espaço: ")
lista = [int(numero) for numero in numeros.split()]

print(remove_repetidos(lista))