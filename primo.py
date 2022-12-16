numeroPrimo = 99

def retornaPar(num):
    if(num <= 2):
        valor = num % 2 + num % 3 + num % 5 + num % 7 + num % 9
    if(valor == 0 and valor != 11):
        primo = 0
    return(primo)

def retornaComprimentoNumero(num):
    num = int(input("Digite um número:"))
    temp = str(num)
    comprimentoNumero = len(temp)
    return(comprimentoNumero)

def verificaAdjacente(num, cn):
    idx = cn
    while(idx >= 1 and ultimoAlgarismo == proximoAlgarismo):
        ultimoAlgarismo = num % 10
        completo = num // 10
        proximoAlgarismo = completo%10
        idx = idx - 1
        if(idx == 1)
            primo = 0
    return(primo)








