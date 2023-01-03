import random
def numeroPecasIniciais():
    while True:
        numeroPecasIniciais = random.randrange(41)
        if(numeroPecasIniciais > 11):
            break
    return (numeroPecasIniciais)
def numeroMaximoPecasRetirar():
    while True:
        numeroMaximoPecasRetirar = random.randrange(5)
        if (numeroMaximoPecasRetirar > 0):
            break
    return(numeroMaximoPecasRetirar)
def tipoJogo():
    print("Bem-vindo ao jogo NIM! Escolha: ")
    print()
    while True:
        print("1 - para jogar uma partida isolada")
        print("2 - para jogar um campeonato")
        tipoJogo = int(input())

        if (tipoJogo == 1):
            print("!!!Você escolheu jogar uma partida única!!!")
            break
        elif (tipoJogo == 2):
            print("!!!Você escolheu jogar um campeonato com 3 partidas!!!")
            break
        else:
            print("!!!Digite 1 ou 2 !!!")
    return(tipoJogo)

def campeonato():
    idxCampeonato = 0
    jogador1 = 0
    jogador2 = 0
    while (idxCampeonato < 3):
        vencedorCampeonato = partida()
        if(vencedorCampeonato == 0):
            jogador1 =+ 1
        elif(vencedorCampeonato == 1):
            jogador2 =+ 1

        if( jogador1 == 2):
            return(0)       ### 0 = computador
        elif(jogador2 == 2):
            return(1)       ### 1 = usuário

def computador_escolhe_jogada(n):
    ################################
    ####### Jogo Computador ########
    nJogada = n
    k = nJogada % 2
    remove = random.randrange(2)
    if(remove == 0):
       remove = 1
    nJogada = nJogada - remove

    return(nJogada)

def usuario_escolhe_jogada(n, m):
    nJogada = n
    verificaValor = numeroMaximoPecasRetirar()

    while True:
        mJogada = int(input("Quantas peças você quer tirar?(Retire no mínimo 1 peça e no máximo 5)"))
        if(mJogada > verificaValor):
            print("Informe um valor entre 1 e 5")
        else:
            break
    nJogada = nJogada - mJogada

    return(nJogada)

def partida():
    n = numeroPecasIniciais()
    m = numeroMaximoPecasRetirar()
    tipoPartida = tipoJogo()
    vencedor = 3

    print("#################Começo do Jogo#################")
    print()
    print("O jogo vai comçar com %d " %n + "peças")
    print("Você pode tirar até %d" %m + " peças por jogada.")
    print()
    print("################################################")



    ######################FIM PROGRAMA###################################

    if(tipoPartida == 1):
        vencedor = partida(n, m)
    elif(tipoPartida == 2):
        vencedor = campeonato( )

    return(vencedor)







