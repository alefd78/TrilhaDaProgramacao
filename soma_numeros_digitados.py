
print("Digite uma sequência, e zero para encerrar!")
soma = 0
multiplicacao = 1

while True:
    numero = int(input("Digite um número: "))
    if (numero == 0):
        break
    soma = soma + numero
print("A soma dos números é %d" %soma)

