def cria_matriz(num_linhas, num_colunas, valor):
    '''
    :param num_linhas: int - número de linhas que a matriz terá.
    :param num_colunas: int - número de colunas que a matriz terá.
    :param valor: int - valor que preencherá os campos da matriz
    :return: matriz  preenchida.
    '''
    matriz = [] #Matriz vazia
    for i in range(num_linhas):
        #Cria a linha i
        linha = [] #Lista vazia
        for j in range(num_colunas):
            linha.append(valor)
    #Adiciona linha à matriz
    matriz.append(linha)

    return matriz
