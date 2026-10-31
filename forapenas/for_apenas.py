# while funciona enquanto a condição for verdadeira.
# for percorre uma sequência ou intervalo.
lista = ["batata", "batata frita", "batata batata", "batata sortida", "Sr.Batata", "Sra.Batata"]

quantidade = len(lista)
print("Quantidade de itens:", quantidade)

for posicao in range(quantidade):
    print(posicao + 1, "-", lista[posicao])

# A posição (índice) de uma lista começa em 0.
