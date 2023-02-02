x = int(input("Informe o primeiro número: "))
y = int(input("Informe o segundo número: "))
z = int(input("Informe o terceiro número: "))

if((x < y) and (y < z)):
    print("crescente")
else:
    print("não está em ordem crescente")