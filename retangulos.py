linhas = int(input("Infomre quantas colunas o retangulo deve ter: "))
colunas = int(input("Informe quantas linhas o retângulo deve ter: "))
x = 1
y = 1

while( y <= colunas ):

    while (x <= linhas):
       print("#", end = "" )
       x = x + 1
    x = 1
    print()
    y = y + 1


