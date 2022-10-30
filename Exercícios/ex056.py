total = 0
qntd = 0
idade2 = 0
nome2 = 0
for var in range(0,4):

    print(f"+=+=+=+=+=+{var + 1}ª PESSOA=+=+=+=+=+=+")
    nome = str(input("Nome: ")).strip()
    idade = int(input("Idade: "))
    sexo = str(input("Sexo[M/F]: ")).strip().lower()
    total = total + idade

    if sexo == "f" and idade < 20:
        qntd = qntd + 1

    if sexo == "m":
        if var == 1:
            idade2 = idade
            nome2 = nome
        else:
            if idade > idade2:
                idade2 = idade
                nome2 = nome
media = total / 4
print(f"A média de idade é {media}")
print(f"Temos {qntd} Mulheres com menos de 20 anos.")
print(f"O nome do homen mais velho tem {idade2} anos e se chama {nome2}")
