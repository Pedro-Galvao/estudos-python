# Exercício de aprendizagem de Python.
print("=== SISTEMA DE COMPRA ===")

saldo = float(input("Digite seu saldo: R$ "))
valor_produto = float(input("Digite o valor do produto: R$ "))
cliente_vip = input("Você é cliente VIP? (S/N): ")
vip = cliente_vip.upper() == "S"

while saldo <= 0:
    print("Saldo inválido!")
    saldo = float(input("Digite seu saldo novamente: R$ "))

desconto = 10 if vip else 0
valor_desconto = valor_produto * (desconto / 100)
valor_final = valor_produto - valor_desconto

if saldo >= valor_final:
    saldo -= valor_final
    print("\nCompra realizada!")
    print("Valor original: R$", valor_produto)
    print("Desconto:", desconto, "%")
    print("Valor final: R$", valor_final)
    print("Saldo restante: R$", saldo)
else:
    print("\nSaldo insuficiente!")

print("Programa encerrado.")
