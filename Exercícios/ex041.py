from datetime import date
while True:
    #Passo 1 ler o ano de nascimento
    print("\033[1;97m=+=" * 15)
    print("CADASTRE UMA PESSOA")
    print("=+=" * 15)
    nascimento = int(input("\033[1;32mDigite o ano de nascimento: "))
    #Passo 2 descobrir a idade
    ano_atual = date.today().year
    idade = ano_atual - nascimento
    #Passo 3 Mostrar sua classificação de acordo com a idade:
    #Passo 3.1 Se for menor ou igual a 9 anos mostre a categoria mirim
    if idade > 0:
        print("\033[1;34m")
    if idade <= 9:
        print(f"Com {idade} anos de idade sua categoria é MRIRIM")
    #Passo 3.2 Se for maior que 9 e menor ou igual 14 mostre sua categoria infantil
    elif idade > 9 and idade <=14:
        print(f"Com {idade} anos de idade sua categoria é INFANTIL")
    #Passo 3.3 Se for maior que 19 e menor ou igual a 19 mostre sua categoria junior
    elif idade > 14 and idade <= 19:
        print(f"Com {idade} anos de idade sua categoria é JUNIOR")
    #Passo 3.4 Se for maior que 19 e menor ou igual a 23 mostre sua categoria senior
    elif idade > 19 and idade <= 23:
        print(f"Com {idade} anos de idade sua categoria é SENIOR")
    #Passo 3.5 Se for maior que 23 mostre sua categoria master
    elif idade > 23:
        print(f"Com {idade} anos de idade sua categoria é MASTER")
    opcao = " "
    while opcao not in "SN":
        opcao = str(input("\033[1;33mDeseja continuar cadastrando mais pessoas? [S/N]: ")).strip().upper()[0]
    if opcao == "N":
        break
print("\033[1;97mPROGRAMA CADASTRO FINALIZADO!")
