numero = int(input("\033[1;33mDigite um número inteiro: "))
while True:
    #PAsso 2 Mostrar o menu de conversão para o usuario
    print("=+=" * 15)
    print("""\033[1;32m
    [1] Para Octal
    [2] Para Decimal
    [3] Para Binario
    [4] Novo número
    [0] Para encerrar o programa
    """)
    #Passo 3 Perguntar a opção do usuario
    opcao = int(input("\033[1;34mDigite sua opção: "))
    #Passo 4 converter para octal,decimal e binario
    if opcao == 1:
        print(f"\033[1;32mO número {numero} para Octal seria {oct(numero)[2:]}")
    elif opcao == 2:
        print(f"\033[1;32mO número {numero} para Decimal seria {hex(numero)[2:]}")
    elif opcao == 3:
        print(f"\033[1;32mO número {numero} para Binario seria {bin(numero)[2:]}")
    elif opcao == 4:
        numero = int(input("\033[1;33mDigite um número inteiro: "))
    elif opcao == 0:
        break
    else:
        print("\033[1;31mOPÇÃO INVALIDA! TENTE NOVAMENTE!")
print("PROGRAMA CONVERSOR DE BASES NÚMERICAS ENCERRADO!")
