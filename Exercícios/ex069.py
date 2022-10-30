cont18 = contman = contwoman = 0
#Passo 1 Ler idade e sexo de varias pessoas
while True:
    print("=+=" * 15)
    print("CADASTRE UMA PESSOA")
    print("=+=" * 15)
    idade = int(input("Idade: "))
    if idade > 18:
        cont18 += 1
    sexo = str(input("Sexo [M/F]: ")).strip().upper()[0]
    #Caso digite errado o sexo
    while sexo not in "FM":
        sexo = str(input("Sexo: ")).strip().upper()[0]
    if sexo == "M":
        contman += 1
    else:
        if idade < 20:
            contwoman += 1
#Passo 2 A cada registro perguntar se deseja continuar ou não
    opcao = str(input("Deseja continuar? [S/N]: ")).strip().upper()[0]
    #Caso digite errado a opção
    while opcao not in "SN":
        opcao = str(input("Deseja continuar? [S/N]: ")).strip().upper()[0]
#Passo 3 Se deseja não finalize o programa
    if opcao == "N":
        break
print(f"Temos {cont18} pessoas maiores de 18 anos")
print(f"Temos {contman} homens")
print(f"Temos {contwoman} mulheres com menos de 20 anos.")
