idade = int(input("Digite sua idade: "))

if idade < 0 or idade >= 120:
    print("Sua idade é inválida.")
elif idade <= 11:
    print("Essa pessoa é criança.")
elif idade <= 17:
    print("Essa pessoa é adolescente.")
elif idade <= 59:
    print("Essa pessoa é adulta.")
else:
    print("Essa pessoa é idosa.")
