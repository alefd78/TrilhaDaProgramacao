import math

a = int(input("Informe o valor de a: "))
b = int(input("Informe o valor de b: "))
c = int(input("Informe o valor de c: "))

delta = b**2 - 4*a*c

if (delta == 0):
    x1 = ((-b) + math.sqrt(delta)) / (2*a)
    print("A única raiz é: %.2f" %x1)
elif (delta < 0):
    print("Esta equação não possui raízes reais")
else:
    x1 = ((-b) + math.sqrt(delta)) / (2*a)
    x2 = ((-b) - math.sqrt(delta)) / (2*a)
    print("X1 é %.2f" %x1)
    print("X2 é %.2f" %x2)


