votos = {"1": 0, "2": 0, "3": 0}
print("VAMOS INICIAR A ELEIÇÃO!")
print("Opções de voto: 1, 2 ou 3")

eleitor = 1
while eleitor <= 10:
    voto = input(f"Eleitor {eleitor}, digite seu voto: ")
    if voto in votos:
        votos[voto] += 1
        eleitor += 1
    else:
        print("Digite um número válido.")

for candidato, total in votos.items():
    print(f"Candidato {candidato}: {total} voto(s)")

maior = max(votos.values())
vencedores = [c for c, total in votos.items() if total == maior]
if len(vencedores) == 1:
    print(f"Candidato {vencedores[0]} foi eleito com {maior} voto(s).")
else:
    print("Houve empate entre os candidatos:", ", ".join(vencedores))
