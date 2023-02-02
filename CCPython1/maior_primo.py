def maior_primo(x):
    primo = True
    num = x
    verifica2 = num
    while(num >= 2):


        if(num == 2):
            return(num)
        elif (num % 2 == 0 and num > 2):
            primo = False
            num = num - 1
        elif(num % 3 == 0 and num != 3):
            primo = False
            num = num - 1
        elif(num % 5 == 0 and num != 5):
            primo = False
            num = num - 1
        elif(num % 7 == 0 and num != 7):
            primo = False
            num = num - 1
        elif(num % 11 == 0 and num != 11):
            primo = False
            nnum = num - 1
        elif(num % 13 == 0 and num != 13):
            primo = False
            num = num - 1
        elif(num % 17 == 0 and num != 17):
            primo = False
            num = num - 1
        elif(num % 19 == 0 and num != 19):
            primo = False
            num = num - 1
        elif(num % 23 == 0 and num != 23):
            primo = False
            num = num - 1
        elif(num % 29 == 0 and num != 29):
            primo = False
            num = num - 1
        elif(num % 37 == 0 and num != 37):
            primo = False
            num = num - 1
        elif(num % 41 == 0 and num != 41):
            primo = False
            num = num - 1
        elif (num % 43 == 0 and num != 41):
            primo = False
            num = num - 1
        elif (num % 47 == 0 and num != 41):
            primo = False
            num = num - 1
        elif (num % 53 == 0 and num != 53):
            primo = False
            num = num - 1
        elif (num % 59 == 0 and num != 59):
            primo = False
            num = num - 1
        elif (num % 61 == 0 and num != 67):
            primo = False
            num = num - 1
        elif (num % 67 == 0 and num != 67):
            primo = False
            num = num - 1
        elif (num % 71 == 0 and num != 71):
            primo = False
            num = num - 1
        elif (num % 73 == 0 and num != 73):
            primo = False
            num = num - 1
        elif (num % 79 == 0 and num != 79):
            primo = False
            num = num - 1
        elif (num % 83 == 0 and num != 83):
            primo = False
            num = num - 1
        elif (num % 89 == 0 and num != 89):
            primo = False
            num = num - 1
        elif (num % 97 == 0 and num != 97):
            primo = False
            num = num - 1
        elif (num % 101 == 0 and num != 101):
            primo = False
            num = num - 1

        else:
            return num
numero = int(input("informe num numero: "))
resposta = maior_primo(numero)
print(resposta)

