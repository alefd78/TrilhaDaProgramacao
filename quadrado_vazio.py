largura = int(input("Informe quantas linhas o retângulo deve ter: "))
altura = int(input("Infomre quantas colunas o retangulo deve ter: "))
rect = ''
for i in range(altura):
	for j in range(largura):
		if(j == 0 or j == largura-1 or i == 0 or i == altura-1):
			rect += '#'
			continue
		rect += ' '
	rect += '\n'
print(rect)