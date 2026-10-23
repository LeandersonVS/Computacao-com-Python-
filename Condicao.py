a = 2
b = 0
c = 0

if a > 0:
    if b > 0:
        print("Tudo ok para decolagem!")
    else:
        print("Tanque principal vazio; voando com combustível reserva!")
else:
    if c > 0:
        print("Foguete não tem piloto, mas há outros foguetes disponíveis!")
    else:
        print("Sem condições para decolar.")