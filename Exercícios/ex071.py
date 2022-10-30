sacar = int(input("Digite o valor que deseja sacar R$:")) #input perguntando o valor do saque
cedula = 50 #cedula recebe 50
total = sacar #total recebe sacar
contando = 0 #contando recebe 0
while True: #equanto for verdade
    if total >= cedula: #se total for maior ou igual que cedula
        total = total - cedula #total recebe ele mesmo menos cedula
        contando += 1 #contando recebe 1a cada repetição
    else: #senão
        if contando > 0: #se contando for maior que 0
            print(f"{contando} Notas de R${cedula}")#imprima na na tela contando e cedula
        if cedula == 50: #se cedula for igual a 50
            cedula = 20#cedula é retornavel com valor 20
        elif cedula == 20:#senão se cedula for igual a 20
            cedula = 10#cedula recebe 10
        elif cedula == 10:#senão se cedula for igual a 10 
            cedula = 1#cedula recebe 1
        contando = 0 #contando recebe 0
        if total == 0: #se total que é o valor do saque for igual a 0
            break #interrompa
