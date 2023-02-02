multiplicacao = 1
numero = 1

while True:

    multiplicacao = multiplicacao * numero
    numero = int(input("Digite um número: "))

    if (numero == 0):
        break


print('A multiplicação dos números é %d' % multiplicacao)