idade = int(input("Informe sua idade: "))

if(idade < 16):
    print("Vocë tem %i de idade, ainda é uma criança." %idade)
elif(idade < 18):
    print("Vocë tem %i de idade, já é adolecente." %idade)
else:
    print("Você tem %i de idade, já é adulto." %idade)