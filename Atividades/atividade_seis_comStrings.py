lista = ["maca", "banana", "abacaxi", "melancia", "jabuticaba", "melao", "tangerina", "laranja", "uva", "mamao", "pera", "filo", "castanha", "berinjela", "mandioca", "tomate", "joaobolao", "ype", "pokan", "cajamanga", "manga", "kiwi"]

for item in lista:
    tamanho = len(item)
    if tamanho % 2 == 0:
        print(f"O item foi: {item}; seu tamanho ({tamanho}) é par")
    else:
        print(f"O item foi: {item}; seu tamanho ({tamanho}) é ímpar")
