import random

pokemons = ["Pikachu", "Bulbassauro", "Squirtle", "Charmander"]
while True:
    escolha = input(f"Escolha um Pokémon {pokemons}: ").strip().title()
    if escolha in pokemons:
        vida = random.randint(20, 200)
        ataque = random.randint(20, 200)
        print(f"Pokémon: {escolha} | Vida: {vida} | Ataque: {ataque}")
        break
    print("Você digitou algo errado. Escolha novamente.")

print("A batalha irá começar! Veja qual inimigo você enfrentará.")
inimigos = ["Rattata", "Zubat", "Pidgey"]
inimigo = random.choice(inimigos)
vida_inimigo = random.randint(20, 200)
ataque_inimigo = random.randint(20, 200)
print(f"Inimigo: {inimigo} | Vida: {vida_inimigo} | Ataque: {ataque_inimigo}")
