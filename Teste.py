def fatorial(n) :
    fat = 1
    while (n > 1):
        fat = fat * n
        n = n - 1
    return fat 

if __name__ == "__main__":
    numero = int(input("Digite o valor de n: "))
    print(fatorial(numero))