from random import randint
vitoria = 0
print("=+=" * 15)
print("VAMOS JOGAR PAR OU IMPAR")
print("=+=" * 15)
#Passo 1 Fazer o computador jogar um número
while True:
    computador = randint(1,10)
#Passo 2 Fazer o jogador digitar um número
    jogador = int(input("Digite um número: "))
#Passo 3 Perguntar ao jogador se ele deseja par ou impar
    opcao = str(input("PAR ou IMPAR? [P/I]: ")).strip().upper()[0]
#Passo 4 Somar os numeros jogados
    soma = computador
    soma += jogador 
#Passo 5 Verificar se a soma é par ou impar
    print("=+=" * 25)
    print(F"O jogador jogou {jogador} e o computador jogou {computador}. A soma entre eles foi igual a {soma}.",end= " ")
    print("DEU PAR" if soma % 2 == 0 else "DEU IMPAR")
    print("=+=" * 25)
    if soma % 2 == 0:
        #Passo 7.1 Mostre uma mensagem de vitoria e conte a vitoria
        if opcao[0] == "P":
            print("YOU WINS!!!")
            vitoria += 1
        else:
            #Passo 6 Se ele perder,pare o programa
            print("YOU LOSER!!!")
            break
    if soma % 2 == 1: 
        #Passo 7.1 Mostre uma mensagem de vitoria e conte a vitoria
        if opcao[0] == "I":
            print("YOU WINS!!!")
            vitoria += 1
        else:
            #Passo 6 Se ele perder,pare o programa
            print("YOU LOSER!!!")
            break
#Passo 8 Mostrar quantas vitorias consecutivas teve quando programa encerrar
print(f"Você teve {vitoria} consecutivas!")
print("=+=" * 15)
