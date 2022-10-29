while True:
    #Passo 1 Ler três retas
    print("\033[1;97m=+=" * 15)
    print("ANALISANDO UM TRIANGULO!")
    print("=+=" * 15)
    reta1 = float(input("\033[1;32mDigite a 1° reta: "))
    reta2 = float(input("Digite a 2° reta: "))
    reta3 = float(input("Digite a 3° reta: "))
    #Passo 2 Saber se pode formar um triangulo
    if reta1 + reta2 > reta3 and reta1 + reta3 > reta2 and reta3 + reta2 > reta1:
        print(f"\033[1;34mCom estas retas você PODE formar um triangulo!")
    #Passo 3 se formar um triangulo mostrar seu tipo:
        #Passo 3.1 Escaleno todos os lados diferentes
        if reta1 != reta2 and reta2 != reta3 and reta1 != reta3:
            print("ESTE TRIANGULO É ESCALENO")
        #Passo 3.2 Equilatero todos os lados iguais
        elif reta1 == reta2 and reta2 == reta3:
            print("ESTE TRIANGULO É EQUILATERO")
        #Passo 3.3 Isoceles dois lados iguais
        elif reta1 == reta2 or reta2 == reta3 or reta1 == reta3:
            print("ESTE TRIANGULO É ISOCELES")
        opcao = " "
        while opcao not in "SN":
            opcao = str(input("Desje acontinaur? [S/N]: ")).strip().upper()[0]
        if opcao[0] == "N":
             break
    else:
        print(f"\033[1;31mCom estas retas você NÃO PODE formar um triangulo!")
        break
print("\033[1;97mPROGRAMA FINALIZADO!")
