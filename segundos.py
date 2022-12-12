segundos = int(input("Por favor, entre com o número de segundos que deseja converter: "))
dias = segundos // 86400
horas = (segundos % 86400)//3600
minutos = (segundos - (dias * 86400) - (horas * 3600)) // 60
segundos = (segundos - (dias * 86400) - (horas * 3600)) % 60
print("%d dias" %dias + ", %d horas" %horas + ", %d minutos" %minutos + " e %d segundos" %segundos +".")