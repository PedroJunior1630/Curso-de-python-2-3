soma = quantos = 0
#Passo 1 Ler varios numeros
while True:
    numero = int(input("Digite um número: "))
#Passo 2 Parar de ler numeros se for digitado 999
    if numero == 999:
        break
#Passo 3 Mostrar esses passos abaixos desconsiderando o flag
    else:
    #Passo 3.1 A soma entre eles
        soma += numero
    #Passo 3.2 Quantos numeros foram digitados
        quantos += 1
print(f"Você digitou {quantos} numeros. A soma foi igual a {soma}")
