#Passo 1 Ler um número
while True:
    print("=+=" * 15)
    numero = int(input("Digite um numero para ver sua tabuada: "))
    print("=+=" * 15)
    #Passo 2 Se o numero digitado for negativo encerrar o programa
    if numero < 0:
        break
    #Passo 3 Senão Mostrar sua tabuada
    else:
        #Passo 3.1 Continuar a ler um numero e mostrar a tabuada
        for tabuada in range(1,11):
            print(f"{numero} X {tabuada} = {numero * tabuada}")
print("=+=" * 15)
print("PROGRAMA TABUADA ENCERRADO")
print("=+=" * 15)
