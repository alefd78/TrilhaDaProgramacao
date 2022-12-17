num = int(input("Digite um número para verificar se é primo:"))
primo = True
if(num == 2):
    primo = True
if(num == 1):
    primo = True
##########################
if (num % 2 == 0 and num == 2):
    primo = True
elif(num % 3 == 0 and num != 3):
    primo = False
elif(num % 5 == 0 and num != 5):
    primo = False
elif(num % 7 == 0 and num != 7):
    primo = False
elif(num % 11 == 0 and num != 11):
    primo = False
elif(num % 13 == 0 and num != 13):
    primo = False
elif(num % 17 == 0 and num != 17):
    primo = False
elif(num % 19 == 0 and num != 19):
    primo = False
elif(num % 23 == 0 and num != 23):
    primo = False
elif(num % 29 == 0 and num != 29):
    primo = False
elif(num % 37 == 0 and num != 37):
    primo = False
elif(num % 41 == 0 and num != 41):
    primo = False

if(primo):
    print("primo")
else:
    print("não primo")














