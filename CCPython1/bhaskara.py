import math

a = int(input("Informe o valor de a: "))
b = int(input("Informe o valor de b: "))
c = int(input("Informe o valor de c: "))

delta = b**2 - 4*a*c

if (delta == 0):
    x1 = ((-b) + math.sqrt(delta)) / (2*a)
    print("a raiz dupla desta equação é %f" %x1)
elif (delta < 0):
    print("esta equação não possui raízes reais")
else:
    x1 = ((-b) + math.sqrt(delta)) / (2*a)
    x2 = ((-b) - math.sqrt(delta)) / (2*a)
    if (x1 < x2):
        print("as raízes da equação são %f" %x1 + "e" "%f" %x2)
    else:
        print("as raízes da equação são %f" %x2 + " e " "%f" %x1)


