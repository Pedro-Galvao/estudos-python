usuario = "admin"
senha = "12345"
usuario_logado = False
tentativa = 0

while not usuario_logado and tentativa < 3:
    usuario_digitado = input("Digite seu usuário: ")
    senha_digitada = input("Digite a senha: ")
    if usuario == usuario_digitado and senha == senha_digitada:
        print("Acesso liberado.")
        usuario_logado = True
    else:
        print("Login incorreto. Tente novamente.")
        tentativa += 1

if not usuario_logado:
    print("Suas tentativas acabaram. Tente novamente mais tarde.")
