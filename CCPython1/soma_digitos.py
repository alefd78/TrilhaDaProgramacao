
num = int(input("Digite um número:"))
temp = str(num)
idx = len(temp)
soma = 0
while idx >= 0:
    soma = num % 10 + soma
    num = num // 10
    idx = idx -1
print (soma)





