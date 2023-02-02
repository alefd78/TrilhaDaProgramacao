num = int(input("Digite um número:"))
temp = str(num)
comprimentoNumero = len(temp)
verificador = False

while (comprimentoNumero > 1):
    ultimoAlgarismo = num % 10
    completo = num // 10
    proximoAlgarismo = completo % 10
    comprimentoNumero -= 1
    num = completo
    if (ultimoAlgarismo == proximoAlgarismo):
        print("sim")
        break
else : print("não")  #else da instrução while !!! Novidade // Do while
















