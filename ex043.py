while True:
    #Passo 1 Ler peso e altura
    print("\033[1;36m=+=" * 15)
    peso = float(input("Peso(KG): "))
    altura = float(input("Altura(M): "))
    print("=+=" * 15)
    #Passo 2 calcular imc
    imc = peso / (altura * altura)
    #Passo 3 dizer as condições de acordo com o imc
    if imc < 18.5:
        print(f"\033[1;33mSeu imc é {imc:.2f},você esta ABAIXO DO PESO!")
    elif imc >= 18.5 and imc <= 25:
        print(f"\033[1;34mSeu imc é {imc:.2f},você esta no peso NORMAAL!")
    elif imc > 25 and imc <= 30:
        print(f"\033[1;33mSeu imc é {imc:.2f},você esta com SOBREPESO!")
    elif imc > 30 and imc <= 40:
        print(f"\033[1;;31mSeu imc é {imc:.2f},você esta com OBESIDADE!")
    elif imc > 40:
        print(f"\033[1;31mSeu imc é {imc:.2f},você esta com SOBREPESO!")
    opcao = " "
    while opcao not in "SN":
        opcao = str(input("\033[1;33mDeseja registrar novamente? [S/N]: ")).strip().upper()[0]
    if opcao == "N":
        break
print("\033[1;97mPROGRAMA IMC FINALIZADO")
