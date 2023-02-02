######## Le números digitados até o usuário digitar um número negativo, calcula a média da soma dos números digitados
#Imprime quantos números foram digitados e a soma dos valores

numero = 0
cont = 0
media = 0
soma = 0
numero = int(input("Digite um número: "))

while(numero > 0):
    soma = soma + numero
    cont +=1
    numero = int(input("Digite um número: "))

media = soma/cont

print("A soma de todos os número é: %d" %soma)
print("O total de valores digitados é: %d" %cont)
print("A média é %.2f" %media)
