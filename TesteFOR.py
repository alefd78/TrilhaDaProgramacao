#######Crescente
for(index) in range(10):
    print(index)
print(index+1)

#######Decrescente
for(index) in range(10, 0, -1):
    print(index)
print(index-1)

########Com Lista

computador = ['Processador', 'Teclado', 'Mouse']
for item in computador:
    print(item)

##########Com dicionário
notas = { 'Português': 7,
          'Matemática':9,
          'Lógica': 8,
          'Algoritmo': 10
          }
for x in notas.values():
    print(x)

for x, y in notas.items():
    print(x, y)
