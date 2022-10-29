produto = float(input("\033[1;32mDigite o preço R$: "))
while True:
    #Passo 1 Ler um valor de um produto
    #Passo 2 Mostrar o menu de pagamento
    print("\033[1;97m=+=" * 15)
    print("""
    [1] Á vista dinheiro/cheque
    [2] Á vista no cartão
    [3] 2X no preço normal
    [4] 3X ou mais
    [5] Outro produto
    [0] Finalizar o programa
    """)
    print("=+=" * 15)
    #Passo 3 perguntar a forma de pagamento
    pagamento = int(input("\033[1;32mDigite sua forma de pagamento: "))
    if pagamento > 0:
        print("\033[1;34m")
    if pagamento == 1:
        produto = produto - (produto * 10 / 100)
        print(f"Com a condição de pagamento Á vista dinheiro/cheque seu produto custará R${produto}")
    elif pagamento == 2:
        produto = produto - (produto * 5 / 100)
        print(f"Com a condição de pagamento Á vista no cartão seu produto custará R${produto}")
    elif pagamento == 3:
        print(f"Com a condição de pagamento 2X parcelado seu produto custará R${produto}")
    elif pagamento == 4:
        parcela = int(input("Quantas vezes parcelado? "))
        produto = produto + (produto * 20 / 100)
        parcelas = produto / parcela
        print(f"Com a condição de pagamento parcelada em {parcela}X de R${parcelas} dando um total de R${produto}")
    elif pagamento == 5:
        produto = float(input("\033[1;32mDigite o preço R$: "))
    elif pagamento == 0:
        break
print("\033[1;97mPROGRAMA FINALIZADO COM SUCESSO!")
