vetor = []
vetorIdx1 = 0
vetorIdx2 = 0
numeroAnterior = 777888
numeroDigitado = 888777

while True:

    numeroAnterior = int(input("Informe um número 1: "))

    if(numeroAnterior == numeroDigitado):
        vetor.append(numeroAnterior)
        print("Possui números Adjacentes!")
        print(vetor)
        break

    numeroDigitado = int(input("Informe o próximo número 2: "))

    if ( numeroAnterior != numeroDigitado):
        vetor.append(numeroAnterior)
        vetor.append(numeroDigitado)

        vetorIdx1 = len(vetor) - 2
        vetorIdx2 = len(vetor)

        #print("LenVetor = %d" %len(vetor))
        #print("vetorIdx1 = %d" %vetorIdx1 + " vetorIdx2 = %d" %vetorIdx2)
    else:
        vetor.append(numeroAnterior)
        vetor.append(numeroDigitado)
        print(vetor)
        print("Possui números Adjacentes!")
        break














