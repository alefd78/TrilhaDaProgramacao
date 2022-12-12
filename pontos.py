import math

x1 = int(input("Informe a referência x1: "))
y1 = int(input("Informe a referência y1: "))

x2 = int(input("Informe a referência x2: "))
y2 = int(input("Informe a referência y2: "))

dx = (x1 - x2)**2
dy = (y1 - y2)**2
d = dx+dy

distancia = math.sqrt(d)

if(distancia >= 10):
    print("longe")
else:
    print("perto")