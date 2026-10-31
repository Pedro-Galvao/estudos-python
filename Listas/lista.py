import random

lista_de_frutas = ["maçã", "banana", "uva"]
print(lista_de_frutas)
print("Fruta sorteada:", random.choice(lista_de_frutas))

lista_de_nomes = ["Alberto", "Pedro", "Galvão"]
indice = random.randint(0, len(lista_de_nomes) - 1)
print("Índice sorteado:", indice)
print("Nome sorteado:", lista_de_nomes[indice])
