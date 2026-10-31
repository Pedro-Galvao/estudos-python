print("Seja bem-vindo à atividade três, vamos revisar alguns conceitos já feitos!")
print("=" * 74)

var_um = input("Digite um valor para virar uma string: ")
print("Esse valor virou uma string: " + str(var_um))
print("=" * 44)

var_dois = input("Digite uma string para virar um número inteiro: ")
print(10 + int(var_dois))
print("=" * 57)

var_tres = bool(input("True or False: "))
if var_tres:
    print(not var_tres)
else:
    print(var_tres)
print("=" * 31)

var_quatro = float(input("Digite um valor para somar com outro número quebrado: "))
print(var_quatro + 0.5)
print("=" * 73)
print("Obrigado pela participação!")
