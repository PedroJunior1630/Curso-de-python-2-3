#Passo 1 Ler o nome e o preço de varios produtos
gasto = produtomil = contador = barato =  0
while True:
    print("=+=" * 15)
    produto = str(input("Nome do produto: "))
    preço = float(input("Preço do produto R$: "))
    print("=+=" * 15)
    contador += 1
#Passo 2 A cada produto e preço deve perguntar se deseja continuar
    opcao = str(input("Deseja continuar? [S/N]: ")).strip().upper()[0]
    while opcao not in "SN":
        opcao = str(input("Deseja continuar? [S/N]: ")).strip().upper()[0]
#Passo 3 Mostrar as estatisticas
    #Passo 3.1 Qual é o gasto total
    gasto += preço
    #Passo 3.2 Quantos produtos custam mais de R$ 1000
    if preço > 1000:
        produtomil += 1
    #Passo 3.3 Qual nome do produto mais barato
    if contador == 1:
        barato = preço
        nome_barato = produto
    else:
        if preço < barato:
            barato = preço
            nome_barato = produto

    if opcao[0] == "N":
        break
print("=+=" * 15)
print(f"Temos o gasto total de R${gasto}")
print(f"Temos {produtomil} produtos acima de R$1000")
print(f"O produto mais barato é a {nome_barato} e custa R${barato}")
print("=+=" * 15)
