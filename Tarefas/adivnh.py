import random

numero_secreto = random.randint(1, 20)
tentativas = 0

print("Bem-vindo ao jogo de adivinhação!")
print("Tente adivinhar o número secreto entre 1 e 20.")
print("-" * 40)

while True:
    try:
        palpite = int(input("Digite seu palpite: "))
    except ValueError:
        print("Digite um número válido.")
        continue

    if palpite < 1 or palpite > 20:
        print("Inválido! Digite um número de 1 a 20.")
        continue

    tentativas += 1
    if palpite == numero_secreto:
        print(f"Você acertou! O número secreto era: {numero_secreto}")
        print(f"Você acertou em {tentativas} tentativas.")
        break
    elif palpite < numero_secreto:
        print("O número secreto é maior.")
    else:
        print("O número secreto é menor.")
