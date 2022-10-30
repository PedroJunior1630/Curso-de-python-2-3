qntd = 0
qntd2 = 0

for var in range(0,6):

    pessoas = int(input(f"{var+1}°Pessoa digite a data de nascimento: "))

    from datetime import date
    ano = date.today().year
    idade = ano - pessoas

    if idade > 20:
        qntd = qntd + 1

    else:
        qntd2 = qntd2 + 1

print(f"Tem {qntd} de maiores.")
print(f"Tem {qntd2} de menores.")
