# Exemplos de print e entrada de dados
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
hobby = input("Digite seu hobby: ")

print("Seu nome é:", nome)
print(f"Você tem {idade} anos e gosta de {hobby}.")

if idade <= 18:
    print("Você é menor de idade ou tem 18 anos.")
else:
    print("Você é maior de 18 anos.")
