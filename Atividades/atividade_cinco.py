# Exercício de aprendizagem de Python.

print("=== SISTEMA DE EMPRÉSTIMO ===")

# O sistema deve analisar se uma pessoa pode ou não receber um empréstimo.
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
salario = float(input("Digite seu salário mensal: R$ "))
valor_emprestimo = int(input("Digite o valor desejado do empréstimo: R$ "))
tem_divida = input("Possui alguma dívida atualmente? (S/N): ")

possui_divida = tem_divida.upper() == "S"

while idade < 18 or idade > 70:
    print("Idade inválida!")
    idade = int(input("Digite sua idade novamente: "))

idade_valida = 18 <= idade <= 70
limite_parcela = salario * 0.30
print("O valor limite pela parcela é:", limite_parcela)

parcela = valor_emprestimo / 24
print("O valor da parcela é:", parcela)

renda_suficiente = parcela <= limite_parcela
aprovado = idade_valida and renda_suficiente and not possui_divida

if aprovado:
    print("Empréstimo aprovado!")
    print(f"Nome do cliente: {nome}")
    print(f"Idade do cliente: {idade}")
    print(f"Valor do empréstimo: R$ {valor_emprestimo:.2f}")
    print(f"Valor da parcela: R$ {parcela:.2f}")
    print(f"Salário: R$ {salario:.2f}")
    print(f"Limite máximo da parcela: R$ {limite_parcela:.2f}")
else:
    print(f"Desculpe {nome}, você não atende aos requisitos para contratar um empréstimo.")

print("\n=== RESULTADO ===")
