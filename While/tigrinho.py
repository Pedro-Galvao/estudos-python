# Simulação de sorteio aleatório para praticar laços e condicionais.
import random

fichas = int(input("Quantas rodadas você quer simular? "))
for rodada in range(1, fichas + 1):
    print(f"\nRodada {rodada}...")
    sorteio = [random.randint(0, 7) for _ in range(3)]
    if sorteio[0] == sorteio[1] == sorteio[2]:
        print("Os três símbolos combinaram!")
    else:
        print("Os símbolos não combinaram desta vez.")
print("Fim da simulação.")
