# Lembre-se que o número máximo de peças que os jogadores podem tirar é m.
#
# O computador sempre joga para que na vez do usuário o número de peças seja da forma k*(m+1), ou seja, algum número múl
# tiplo qualquer de (m+1). Por enquanto vamos aceitar que isso sempre ocorre e depois vou explicar como é possível.
#
# Dito isso, no turno seguinte o jogador vai ficar com (k-1)*(m+1) peças, e no próximo (k-2)*(m+1)... e assim por diante.
# Então, em alguma rodada o jogador vai ter (k-k)*(m+1) peças que é equivalente a 0*(m+1) = 0, ou seja, ele perdeu.
#
# O número de peças na vez do computador é sempre k*(m+1) - j onde j é a jogada do usuário, que varia entre 1 e m.
# Logo, não tem como o usuário deixar (k-1)*(m+1) peças para o computador. O máximo que ele pode deixar é  (k-1)*(m-1) - 1 e o mínimo é (k)*(m+1) - m.
#
# O computador quer deixar (k-1)*(m+1) para o usuário, e pra isso a jogada dele precisa ser
# (m + 1- j) pois k*(m+1) - j - (m+1-j) = k*m + k - j + m - 1 + j = (k-1)*m + k-1 = (k-1)*(m+1).

def computador_escolhe_jogada(n, m):
    nJogadaComputador = n
    mJogadaComputador = m
    kJogadaComputador = 0
    ##############################################
    # Lógica da Jogada         k*(m+1)           #
    ##############################################
    k = n * (m-1)

    return(nJogadaComputador)

def usuario_escolhe_jogada(n, m):
    nJogadaUsuario = n
    mJogadaUsuario = m
    ##############################################
    #Lógica da Jogada do Usuário                 #
    ##############################################
    return(mJogadaComputador)
def campeonato( ):
    idxCampeonato = 0
    vencedorCampeonato = 0
    while(idxCampeonato < 3):
        vencedorCampeonato = partida()
        if(vencedorCampeonato == 0):
            vencedorComputador = 1
        elif(vencedorCampeonato == 1):
            vencedorUsuario = 1
    if(vecedorComputador > vencedorUsuario):
        return(0)
    elif(vencedorUsuario > vencedorComputador):
        return(1)

def partida():
    nPartida = 0
    mPartida = 0
    tipoPartida = 0
    usuarioIniciaJogo = 0
    contVitorioUsuario = 0
    contVitoriaComputador = 0

    nPartida = int(input("Com quantas peças iniciará o jogo: "))
    mPartida = int(input("Qual o número máximo de peças que podem ser retiradas: "))

    usuarioIniciaJogo = (nPartida * mPartida + 1) % 2

    if(usuarioIniciaJogo == 0):
        print("O usuário inicia o jogo")

        while True:
            nPartida = usuario_escolhe_jogada(nPartida, mPartida)


            npartida = computador_escolhe_jogada(nPartida, mPartida)

            if( nPartida < 0):
                break


    elif(usuarioIniciaJogo != 0):
        print("O computador inicia o jogo")

        while True:
            npartida = computador_escolhe_jogada(nPartida, mPartida)

            
            npartida = computador_escolhe_jogada(nPartida, mPartida)




    return(vencedorPartida)


    if(tipoPartida == 1):
        vencedorPartida = partida()
    elif(tipoPartida == 2):
        vencedorPartida = campeonato(nPartida, mPartida)


