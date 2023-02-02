import re


def le_assinatura():

    print("Bem-vindo ao detector automático de COH-PIAH.")

    wal = float(input("Entre o tamanho medio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]


def le_textos():
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) + " (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) + " (aperte enter para sair):")

    return textos


def separa_sentencas(texto):

    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas


def separa_frases(sentenca):

    return re.split(r'[,:;]+', sentenca)


def separa_palavras(frase):

    return frase.split()


def n_palavras_unicas(lista_palavras):

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

    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)


def compara_assinatura(as_a, as_b):

    S = 0
    for i in range(0, 6):
        S = S + (abs(as_a[i] - as_b[i]))
    grau = S / 6
    if grau < 0:
        grau = grau * (-1)
    return grau
    pass


def calcula_assinatura(texto):

    lista_de_palavras = separa_palavras(texto)
    n_total_palavras = len(lista_de_palavras)

    tamanho_palavras = 0
    for i in range(n_total_palavras):
        tamanho_palavras = tamanho_palavras + len(lista_de_palavras[i])

    tamanho_medio_palavra = tamanho_palavras / n_total_palavras

    type_token = n_palavras_diferentes(texto) / n_total_palavras

    hapax_legomana = n_palavras_unicas(texto) / n_total_palavras

    n_total_sentencas = len(separa_sentencas(texto))

    n_total_frases = len(separa_frases(texto))

    tamanho_medio_sentenca = tamanho_palavras / n_total_sentencas

    complexidade_sentenca = n_total_frases / n_total_sentencas

    tamanho_medio_frase = tamanho_palavras / n_total_frases

    assinatura = [tamanho_medio_palavra, type_token, hapax_legomana, tamanho_medio_sentenca, complexidade_sentenca,
                  tamanho_medio_frase]

    return assinatura

    pass


def avalia_textos(textos, ass_cp):

    i = 1
    assinatura_texto = calcula_assinatura(textos[i])
    grau_similaridade = compara_assinatura(assinatura_texto,
                                           ass_cp)


    menor_grau = grau_similaridade
    texto_plageado = i
    i = i + 1
    while i < (len(textos)):
        assinatura_texto = calcula_assinatura(textos[i])
        grau_similaridade = compara_assinatura(assinatura_texto, ass_cp)
        if grau_similaridade < menor_grau:
            menor_grau = grau_similaridade
            texto_plageado = i
        i = i + 1

    print("O autor do texto %d está infectado com COH-PIAH" % (texto_plageado))
    return texto_plageado
    pass


def main():
    assinatura_cp = le_assinatura()
    textos_lidos = le_textos()
    avalia_textos(textos_lidos,
                  assinatura_cp)


main()