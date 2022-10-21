A = int(input("Informe o valor para a variável A: "))
B = int(input("Informe um valor para a variável B: "))

if(A > B):
    AUX = A;
    A = B;
    B = AUX;
print("O valor da variável A é %i" %A)
print("O valor da variável B é %i" %B)

