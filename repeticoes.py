# For = loop que percore sequências, repetindo ações para cada elemento.
# While = loop que executa ações enquanto a condição for verdadeira.
# for x in range(5): = range(5) = [0, 1, 2, 3, 4]
# nesse caso possui 5 itens
notas = []

for x in range(5):
    matricula = input("MT: ")
    nome = input("Nome: ")
    nota = float(input("Nota: "))
    resultado = [matricula, nome, nota]
# append = Ele é uma das operações de manipulação de listas mais comuns e é muito útil quando você precisa expandir uma lista dinâmica ou construir uma lista elemento por elemento.
    notas.append(resultado)
    print("Quantidade de notas", len(notas))

    for n in notas:
        matricula = n[0]
        nota = n[1]
        print("A MT", matricula, nome, "tirou a nota:", nota)

