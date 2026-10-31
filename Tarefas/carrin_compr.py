produtos = {"arroz": 25.00, "feijao": 18.00, "queijo": 30.00, "carne": 39.00, "tomate": 2.50}
print("-------- Produtos disponíveis --------")
for produto, preco in produtos.items():
    print(f"- {produto}: R$ {preco:.2f}")

produto_escolhido = ""
while produto_escolhido not in produtos:
    produto_escolhido = input("Digite o nome do produto escolhido: ").strip().lower()
    if produto_escolhido not in produtos:
        print("Produto indisponível. Tente novamente.")

quantidade = int(input(f"Quantas unidades de {produto_escolhido}? "))
valor_original = produtos[produto_escolhido] * quantidade
desconto = valor_original * 0.10 if valor_original > 100 else 0
valor_final = valor_original - desconto

print("\nResumo da compra")
print(f"Produto: {produto_escolhido}")
print(f"Quantidade: {quantidade}")
print(f"Valor original: R$ {valor_original:.2f}")
print(f"Desconto: R$ {desconto:.2f}")
print(f"Valor final: R$ {valor_final:.2f}")
