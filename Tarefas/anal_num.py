numeros = []
for i in range(8):
    numeros.append(float(input(f"Digite o {i + 1}º número: ")))

positivos = sum(1 for n in numeros if n > 0)
negativos = sum(1 for n in numeros if n < 0)
zeros = sum(1 for n in numeros if n == 0)

print("====== Resultados ======")
print(f"Números positivos: {positivos}")
print(f"Números negativos: {negativos}")
print(f"Zeros: {zeros}")
print(f"Lista de números: {numeros}")
