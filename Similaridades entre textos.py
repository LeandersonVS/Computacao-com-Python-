import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def compara_assinatura(as_a, as_b):
    '''Essa funcao recebe duas assinaturas de texto e devolve o grau de similaridade nas assinaturas.'''
    soma = 0
    for i in range(6):
        soma += abs(as_a[i] - as_b[i])
    return soma / 6

def calcula_assinatura(texto):
    '''Essa funcao recebe um texto e devolve a assinatura do texto.'''
    sentencas = separa_sentencas(texto)

    frases = []
    for sentenca in sentencas:
        frases.extend(separa_frases(sentenca))

    palavras = []
    for frase in frases:
        palavras.extend(separa_palavras(frase))

    total_palavras = len(palavras)

    # 1. Tamanho médio de palavra
    tamanho_medio_palavra = sum(len(p) for p in palavras) / total_palavras

    # 2. Relação Type-Token
    type_token = n_palavras_diferentes(palavras) / total_palavras

    # 3. Razão Hapax Legomana
    hapax = n_palavras_unicas(palavras) / total_palavras

    # 4. Tamanho médio de sentença
    tamanho_medio_sentenca = sum(len(s) for s in sentencas) / len(sentencas)

    # 5. Complexidade de sentença
    complexidade = len(frases) / len(sentencas)

    # 6. Tamanho médio de frase
    tamanho_medio_frase = sum(len(f) for f in frases) / len(frases)

    return [tamanho_medio_palavra, type_token, hapax,
            tamanho_medio_sentenca, complexidade, tamanho_medio_frase]

def avalia_textos(textos, ass_cp):
    '''Essa funcao recebe uma lista de textos e uma assinatura ass_cp e devolve o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    menor_grau = None
    indice_infectado = 0

    for i in range(len(textos)):
        assinatura = calcula_assinatura(textos[i])
        grau = compara_assinatura(assinatura, ass_cp)
        if menor_grau is None or grau < menor_grau:
            menor_grau = grau
            indice_infectado = i + 1

    return indice_infectado

def main():
    assinatura = le_assinatura()
    textos = le_textos()
    infectado = avalia_textos(textos, assinatura)
    print("O autor do texto", infectado, "está infectado com COH-PIAH")

main()