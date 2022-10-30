soma = 0
qntd = 0

print("\033[1;33m=+=" * 15)
print("SOMANDO NÚMEROS PARES")
print("=+=" * 15)

for var in range(0,6):
    numero = int(input(f"\033[1;97mDigite o {var + 1}° valor: "))
    if numero % 2 == 0:
        soma = soma + numero
        qntd = qntd + 1

print(f"\033[1;32mTemos {qntd} números pares no total.")
print(f"\033[1;34mA soma entre eles é igual a {soma}")
