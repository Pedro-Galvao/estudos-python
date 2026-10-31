# Exercício de laços com sorteios aleatórios.
import random

fichas = int(input("Quantas rodadas deseja simular? "))
frutas = ["Maçã", "Banana", "Pera", "Abacaxi", "Melancia"]

for rodada in range(1, fichas + 1):
    fruta = random.choice(frutas)
    resultado = random.randint(1, 5)
    print(f"Rodada {rodada}: fruta sorteada: {fruta}")
    print(f"Resultado da roleta: {resultado}")
    if resultado == 5:
        print(f"Parabéns! Prêmio recebido: {fruta}")
    else:
        print("Não foi dessa vez.")
