idade = int(input("Sua idade: "))
alcool = float(input("Sua taxa de álcool no sangue (0 se sóbrio): "))
cor_semaforo = input("Cor do semáforo na entrada (vermelho/amarelo/verde): ").lower()

if idade < 18:
    print("Menor de idade não entra. Volta pra casa!")
elif alcool > 0.6:
    print("Você está muito bêbado(a)! Segurança vai te colocar num táxi.")
elif cor_semaforo == "vermelho":
    print("Espera aí! O semáforo da entrada está fechado.")
elif cor_semaforo == "amarelo":
    print("Quase lá, mas espera só mais um pouquinho.")
elif cor_semaforo == "verde":
    print("Pode entrar e se divertir com responsabilidade!")
else:
    print("Não entendi a cor do semáforo, tenta de novo.")
