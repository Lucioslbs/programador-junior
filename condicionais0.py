salario = float(input("Informe o salário: "))

if salario <= 3000:
    print("Programador junior")
# elif = entao se, and e para adicionar mais uma condição.
elif salario > 3000 and salario <= 6000:
    print("Programador pleno")
# elif = entao se, and e para adicionar mais uma condição.
elif salario > 6000 and salario <=15000:
    print("Programador senior")
else:
    print("Gerente de projetos")
