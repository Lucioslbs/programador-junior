salario = float(input("Informe o salário: "))

if salario <= 3000:
    print("Programador Junior")
elif salario > 3000 and salario <= 5000:
    print("Programado pleno")
elif salario > 6000 and salario <= 9000:
    print("Programador senior")
else:
    print("Gerente de projetos")
