# Exercícios de aprendizagem: login, senha e limite de tentativas.
usuario = "ADMIN"
senha = "12345"

resposta_usuario = input("Qual seu usuário? ")
resposta_senha = input("Qual sua senha? ")

if resposta_usuario == usuario and resposta_senha == senha:
    print("Login efetuado com sucesso.")
else:
    print("Usuário ou senha incorretos.")

tentativas = 0
while tentativas < 3:
    usuario_digitado = input("Digite seu usuário: ")
    senha_digitada = input("Digite sua senha: ")
    if usuario_digitado == usuario and senha_digitada == senha:
        print("Acesso liberado!")
        break
    tentativas += 1
    print("Login incorreto.")
if tentativas == 3:
    print("Suas tentativas acabaram. Tente novamente mais tarde.")
