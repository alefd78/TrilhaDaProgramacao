num = int(input("Digite um número:"))
temp = str(num)
tamanho = len(temp)
ultimo = 9
primeiro = 99
primo = 0

while tamanho >= 0:
    ultimo = num // 10
    primeiro = num // 10
    if(ultimo == primeiro):
        tamanho = tamanho - 1
        print(primeiro)






