# Solicita ao usuário um número interiro positivo
n = int(input("Digite um número inteiro positivo: "))

# Incializa a soma dos números pares
soma_pares = 0

# usa um loop para iterar pelos números de 1 até n
for numero in range(1, n + 1):
    # Verifica se o número é par
    if numero % 2 == 0:
        # Adiciona o número par à soma
        soma_pares += numero

# Imprime o resultado
print(f"A soma de todos os números pares de 1 até {n} é: {soma_pares}")
