import random

print("Jogo de Adivinhação de Números Aleatórios, para sair digite 'sair'")

while True:
    numero_aleatorio = random.randint(1, 9)
    tentativa = input("Adivinhe o número entre 1 e 9: ")

    if tentativa == "sair":
        break

    tentativa = int(tentativa)
    if tentativa == numero_aleatorio:
        print("Parabéns, você acertou!")
    elif tentativa < numero_aleatorio:
        print("O número é MAIOR.")
    elif tentativa > numero_aleatorio:
        print("O número é MENOR.")

print("Obrigado por jogar!")