# Exercícios sobre tipos, condicionais e entrada de dados.
cor = input("Qual cor o semáforo está? ").strip().lower()

if cor == "verde":
    print("Pode passar!")
elif cor == "amarelo":
    print("Aguarde!")
elif cor == "vermelho":
    print("Pare!")
else:
    print("Cor não reconhecida.")

idade = int(input("Qual sua idade? "))
if idade >= 18:
    print("Você é maior de idade!")
else:
    print("Você é menor de idade!")

bebeu = input("Você bebeu? (sim/não) ").strip().lower()
if idade >= 18 and bebeu == "sim":
    print("Não dirija após beber.")
elif bebeu == "não":
    print("Respeite as regras de trânsito.")
else:
    print("Peça ajuda a um adulto responsável.")
