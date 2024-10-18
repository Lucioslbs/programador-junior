import random

def jogo_adivinhacao():
    numero_secreto = random.randint(1, 100)
    tentativas = 0
    acertou = False

    print("")
    print("**Bem-vindo ao jogo de Adivinhação!**")
    print("")
    print("Estou pensando em um número entre 1 e 100.")
    print("Tente adivinhar qual é o número.")

    while not acertou:
        palpite = int(input("Digite sua tentativa: "))
        tentativas += 1

        if palpite < numero_secreto:
            print("Muito baixo! tente novamente.")
        elif palpite > numero_secreto:
            print("Muito alto! Tente novamente.")
        else:
            acertou = True
            print(f"Parabéns! Você acertou o número em {tentativas} tentativas")

# Iniciar o jogo
jogo_adivinhacao()
