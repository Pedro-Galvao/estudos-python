equipe = [
    ["Pikachu", 120, 150],
    ["Charmander", 90, 200],
    ["Squirtle", 190, 110],
    ["Bulbassauro", 100, 100],
]

print("Escolha seu Pokémon:")
for indice, pokemon in enumerate(equipe):
    print(f"{indice} - {pokemon[0]}")

try:
    opcao = int(input("Qual será sua escolha? "))
    escolhido = equipe[opcao]
    print(f"Nome: {escolhido[0]} | Vida: {escolhido[1]} | Ataque: {escolhido[2]}")
except (ValueError, IndexError):
    print("Opção inválida.")
