largura = int(input("digite a largura: "))
altura = int(input("digite a altura: "))

for linha in range(altura):
    for coluna in range(largura):
        if linha == 0 or linha == altura - 1 or coluna == 0 or coluna == largura - 1:
            print("#", end="")
        else:
            print(" ", end="")
    print()