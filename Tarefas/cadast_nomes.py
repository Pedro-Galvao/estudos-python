nomes = []
for i in range(5):
    nomes.append(input(f"Digite o {i + 1}º nome: "))

print(f"Quantidade de nomes cadastrados: {len(nomes)}")
busca = input("Digite um nome para buscar na lista: ")
if busca in nomes:
    print(f"O nome {busca} está na lista!")
else:
    print(f"O nome {busca} não está na lista.")
