soma = 0
qntd = 0
for var in range(1,501,2):
    if var % 3 == 0:
        qntd += 1
        soma += var
print(f"São {qntd} valores que sua soma é {soma}")
