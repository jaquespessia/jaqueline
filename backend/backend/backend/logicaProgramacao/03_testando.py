salario = int(input("Digite o salário: "))

if salario > 5000:
    print("Classe Alta")
elif salario >=3000 and salario <=4999:
    print("Classe Média")
else:
    print("Classe Baixa")