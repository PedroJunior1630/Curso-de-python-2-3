while True:
    from datetime import date
    #Passo 1 Ler o ano de nascimento
    print("\033[1;97m=+=" * 20)
    nascimento = int(input("\033[1;32mDigite sue ano de nascimento: "))
    #Passo 2 Calcular a idade
    ano = date.today().year
    idade = ano - nascimento

    if idade == 18:
        print("\033[1;33mATENÇÃO VOCÊ TEM 18 ANOS! ESÁ NA HORA DE SE ALISTAR")
    elif idade < 18:
        print(f"\033[1;34mATENÇÃO! VOCÊ TEM {idade} ANOS DE IDADE,IRÁ SE ALISTAR DAQUI A {18 - idade} ANOS EM {ano + (18 - idade)}")
    elif idade > 18:
        print(f"\033[1;31mATENÇÃO VOCÊ TEM {idade} ANOS DE IDADE,ESTÁ A {idade - 18} ANOS ATRASADO! ERA PARA SER ALISTADO EM {ano - idade + 18}")
    opcao = " "
    while opcao[0] not in "SN":
        opcao = str(input("\033[1;32mDeseja continuar? [S/N]: ")).strip().upper()[0]
    if opcao == "N":
        break
print("\033[1;97mPROGRAMA DE ALISTAMENTO ENCERRADO COM SUCESSO!")
