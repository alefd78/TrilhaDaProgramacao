print("Cadastro de dados dos usuários")
nome = input("Informe o nome do usuário: ")
codigo = int(input("Informe o código do usuário: "))
salario = float(input("Informe o salário do usuário: "))
situacao = input("Informe a situaçao do usuário: ")

print("O nome do usuário é %s," %nome + "\nSeu código é %d," %codigo + "\nSeu salário é %.2f," %salario + " \nSua situação é: %s." %situacao)
