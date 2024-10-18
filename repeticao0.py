notas = []

contador = 1

while contador <= 5:
    matricula = input("MT: ")
    nota = float(input("Nota: "))
    resultado = [matricula, nota]
    notas.append(resultado)

    # alternativa: contador += 1
    contador = contador + 1

print("Quantidade de notas", len(notas))
