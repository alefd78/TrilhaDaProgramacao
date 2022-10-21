codigo = 10
salario = 1500.00
nome = 'José'
situacao = True

tipo = type(salario)
print(salario)
print(tipo)

print("Código:", codigo, " Nome:", nome, "O salário atual é de:", salario)
#########################################################################################
print("Código: " + str(codigo)+ " Nome: " + nome + " O salário atual é de: "+ str(salario))
#########################################################################################
print("Código: %d" %codigo)
print("Nome: %s" %nome)
print("Salário autal: %f" %salario)
print("Situação: %r" %situacao)

