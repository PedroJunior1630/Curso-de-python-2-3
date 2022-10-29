while True:
    #Passo 1 Ler dois valores inteiros
    numero1 = int(input("\033[1;34mDigite o ¹° valor inteiro: "))
    numero2 = int(input("Digite o 2° valor inteiro: "))
    #Passo 2 Comparar eles
    if numero1 > numero2:
        print(f"\033[1;32mO maior valor é {numero1}")
    elif numero2 > numero1:
        print(f"\033[1;32mO maior número é {numero2}")
    elif numero1 == numero2:
        print("\033[1;97mAmbos valores são iguais")
    opcao = int(input("Deseja continaur? [1] [0 para encerrar]: "))
    if opcao == 0:
        break
        #Passo 2.1 Primeiro valor maior
        #Passo 2.2 Segundo valor maior
        #Passo 2.3 Ambos são iguais
print("PROGRAMA ENCERRADO COM SUCESSO!")
