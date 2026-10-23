largura = int(input("digite a largura: "))
altura = int(input("digite a altura: "))

for _ in range(altura):
    for _ in range(largura):
        print("#", end="")
    print()