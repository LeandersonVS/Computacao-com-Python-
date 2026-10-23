def computador_escolhe_jogada(n, m):
    if n <= m:
        return n

    for jogada in range(1, m + 1):
        if (n - jogada) % (m + 1) == 0:
            return jogada

    return m


def usuario_escolhe_jogada(n, m):
    jogada = int(input("Quantas peças você vai tirar? "))

    while jogada < 1 or jogada > m or jogada > n:
        print("\nOops! Jogada inválida! Tente de novo.")
        jogada = int(input("\nQuantas peças você vai tirar? "))

    return jogada


def imprimir_estado(jogador, jogada, n):
    if jogada == 1:
        print(f"{jogador} tirou uma peça.")
    else:
        print(f"{jogador} tirou {jogada} peças.")

    if n == 1:
        print("Agora resta apenas uma peça no tabuleiro.")
    elif n > 1:
        print(f"Agora restam {n} peças no tabuleiro.")


def partida():
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))

    vez_do_computador = n % (m + 1) != 0

    if vez_do_computador:
        print("\nComputador começa!")
    else:
        print("\nVocê começa!")

    while n > 0:
        if vez_do_computador:
            jogada = computador_escolhe_jogada(n, m)
            n -= jogada
            imprimir_estado("O computador", jogada, n)

            if n == 0:
                print("Fim do jogo! O computador ganhou!")
                return "computador"
        else:
            jogada = usuario_escolhe_jogada(n, m)
            n -= jogada
            imprimir_estado("Você", jogada, n)

            if n == 0:
                print("Fim do jogo! Você ganhou!")
                return "usuario"

        vez_do_computador = not vez_do_computador


def campeonato():
    pontos_usuario = 0
    pontos_computador = 0

    for rodada in range(1, 4):
        print(f"\n**** Rodada {rodada} ****\n")
        vencedor = partida()

        if vencedor == "usuario":
            pontos_usuario += 1
        else:
            pontos_computador += 1

    print("\n**** Final do campeonato! ****")
    print(f"\nPlacar: Você {pontos_usuario} X {pontos_computador} Computador")

    if pontos_usuario > pontos_computador:
        print("Você venceu o campeonato!")
    else:
        print("O computador venceu o campeonato!")


def main():
    print("Bem-vindo ao jogo do NIM! Escolha:\n")
    print("1 - para jogar uma partida isolada")
    print("2 - para jogar um campeonato")

    opcao = int(input())

    if opcao == 1:
        print("\nVoce escolheu uma partida isolada!")
        partida()
    elif opcao == 2:
        print("\nVoce escolheu um campeonato!")
        campeonato()


if __name__ == "__main__":
    main()