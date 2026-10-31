import random

vida_jogador = 100
vida_inimigo = 100
rodadas = 0

print("====== A batalha acaba de começar! ======")
while vida_jogador > 0 and vida_inimigo > 0:
    rodadas += 1
    print(f"\nRodada: {rodadas}")
    print(f"Sua vida: {vida_jogador} | Vida do inimigo: {vida_inimigo}")
    print("1 - Atacar")
    print("2 - Curar")
    opcao = input("Digite o número da opção: ")

    if opcao == "1":
        dano = random.randint(10, 25)
        vida_inimigo -= dano
        print(f"Você causou {dano} de dano!")
    elif opcao == "2":
        cura = random.randint(5, 15)
        vida_jogador = min(100, vida_jogador + cura)
        print(f"Você recuperou até {cura} pontos de vida.")
    else:
        print("Opção inválida.")

    if vida_inimigo > 0:
        dano_inimigo = random.randint(5, 20)
        vida_jogador -= dano_inimigo
        print(f"O inimigo contra-atacou e causou {dano_inimigo} de dano!")
    else:
        print("O inimigo foi derrotado!")

print("\n================ Fim de jogo ================")
print(f"Quantidade de rodadas: {rodadas}")
if vida_jogador > 0 and vida_inimigo <= 0:
    print("Você venceu! Parabéns!")
elif vida_jogador <= 0 and vida_inimigo <= 0:
    print("Houve um empate!")
else:
    print("Você foi derrotado. Tente novamente.")
