# Percorre uma lista de 20 valores e identifica par ou ímpar.
import random

lista = list(range(1, 21))
numero_escolhido = random.choice(lista)

for numero in lista:
    if numero == numero_escolhido:
        print(f"Esse número foi o que caiu no FOR: {numero}")
        if numero % 2 == 0:
            print(f"Esse número é par: {numero}")
        else:
            print(f"Esse número é ímpar: {numero}")
