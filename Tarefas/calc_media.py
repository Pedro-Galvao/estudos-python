nota_um = float(input("Digite a primeira nota: "))
nota_dois = float(input("Digite a segunda nota: "))
nota_tres = float(input("Digite a terceira nota: "))
nome_aluno = input("Digite o nome do aluno: ")

media = (nota_um + nota_dois + nota_tres) / 3
print(f"Vamos calcular a média de {nome_aluno}.")
print(f"O nome tem {len(nome_aluno)} caracteres.")
print(f"Média do aluno: {media:.2f}")

if media >= 7:
    print("Este aluno está aprovado.")
elif media >= 5:
    print("Este aluno está de recuperação.")
else:
    print("Este aluno está reprovado.")
