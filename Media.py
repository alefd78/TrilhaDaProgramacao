NotaA = float(input("Informe o valor da nota A: "))
NotaB = float(input("Informe o valor da nota B: "))

media = (NotaA + NotaB) / 2
if(media >= 7):
    print("Sua média foi %.2f , Você foi aprovado, parabéns!!!" %media)
else:
    print("Sua média foi %.2f , Você foi reprovado, estude mais!!!" %media)