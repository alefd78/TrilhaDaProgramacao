nome = input("Informe seu nome: ")
diaVencimento = input("Informe o dia do vencimento da fatura: ")
mesVencimento = input("Informe o mês do vencimento da fatura: ")
valorFatura = input("Informe o valor da fatura: ")

print("Olá, %s" %nome)
print("A sua fatura com vencimento em %s " %diaVencimento + "de %s " %mesVencimento + "no valor de R$ %s " %valorFatura + "está fechada.")
