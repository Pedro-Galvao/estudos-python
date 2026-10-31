while True:
    numero = int(input("Digite o valor para gerar a tabuada: "))
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

    decisao = input("Deseja gerar outra tabuada? (S/N): ").strip().lower()
    if decisao != "s":
        break
