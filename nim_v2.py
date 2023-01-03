import random
def computador_escolhe_jogada(n, m):
    nJogada = n
    mJogada = m
    jogadaImpar = 1
    jogadaPar = random.randrange(2)

    if(jogadaPar == 0):
        jogadaPar = 1

    validaJogada = nJogada % 2
    if (validaJogada == 0):
        return(jogadaPar)
    elif(validaJogada != 0):
        return(jogadaImpar)

def usuario_escolhe_jogada(n, m):
    nJogada = n
    mJogada = m
    jogadaUsuario = m
    while True:

        while True:
            jogadaUsuario = int(input("Quantas peças você quer retirar?"))
            if (jogadaUsuario <= mJogada and mJogada > 0):
                print("Valor invalido")
            else:
                break

    return(mJogada)

def campeonato(n, m):
    idx = 1
    vencedor = 1
    computador = 0
    usuario = 0
    while ( idx <= 3):
        vencedor = partida()
        if(vencedor == 0 and idx < 3):
            computador =+ 1
        elif(vencedor == 1 and idx < 3):
            usuario =+ 1

    if(computador >= 2): ### 0 => Computer
        return(0)
    elif(usuario >= 2): ### 1 => User
        return(1)

def partida( ):

    computador = 0
    usuario = 1
    vencedor = 0

    # while True:
    #     nPartida = int(input("Com quantas peças o jogo deve começar: "))
    #     mPartida = int(input("Qual o número máximo de peças que podem ser retiradas: "))
    #      if(mPartida > (nPartida - 2)):
    #          break
    nPartida = int(input("Com quantas peças o jogo deve começar: "))
    mPartida = int(input("Qual o número máximo de peças que podem ser retiradas: "))
    inicioPartida = nPartida%(mPartida - 1)
    if(inicioPartida == 0):
        nPartida =- usuario_escolhe_jogada(nPartida, mPartida)
    else:
        while(nPartida >= 1):

            nPartida =- computador_escolhe_jogada(nPartida, mPartida)
            if(nPartida == 1):
                return( 0 )

            nPartida =- usuario_escolhe_jogada(nPartida, mPartida)
            if(nPartida == 1):
                return(1)

vencedor = partida()
if(vencedor == 0):
    print("computador venceu")
else:
    print("usuario venceu")









