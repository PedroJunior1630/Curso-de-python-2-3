maior = 0
menor = 0

for var in range(1,6):
    peso = float(input("Digite seu peso: "))
    if var == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print(f"O maior peso é {maior}Kg")
print(f"O menor peso é {menor}Kg")
