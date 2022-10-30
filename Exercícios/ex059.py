valor1 = int(input("\033[1;32mDigite o 1° valor: "))
valor2 = int(input("Digite o 2° valor: "))
opcao = 0
while opcao != 5:
    print("""\033[1;33m
    -----------------------
    [1] SOMAR
    [2] MULTIPLICAR
    [3] MAIOR
    [4] NOVOS NÚMEROS
    [5] SAIR DO PROGRAMA
    -----------------------
    """)
    opcao = int(input("\033[1;32mDigite a opção que deseja: "))
    if opcao == 1:
        print(f"\033[1;36m{valor1} + {valor2} = {valor1 + valor2}")
    elif opcao == 2:
        print(f"\033[1;36m{valor1} x {valor2} = {valor1 * valor2}")
    elif opcao == 3:
        print("\033[1;36m")
        if valor1 > valor2:
            print(f"Maior valor: {valor1}")
        elif valor2 > valor1:
            print(f"Maior valor: {valor2}")
        elif valor1 == valor2 or valor2 == valor1:
            print("Ambos são iguais")
    elif opcao == 4:
        valor1 = int(input("\033[1;32mDigite o 1° valor: "))
        valor2 = int(input("Digite o 2° valor: "))
    elif opcao == 0 or opcao > 5:
        opcao = int(input("\033[1;31mERROR! TENTE NOVAMENTE: "))
print("\033[1;97m PROGRAMA FINALIZADO COM SUCESSO!")
