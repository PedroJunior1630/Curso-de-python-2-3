while True:
    #Passo 1 ler duas notas de um aluno
    nota1 = float(input("\033[1;32mDigite a 1° nota[-1 para encerrar o programa]: "))
    if nota1 < 0:
        break
    nota2 = float(input("Digite a 2° nota: "))
    materia = str(input("Dgite a materia: ")).strip().capitalize()
    #Passo 2 calcular a média
    media = (nota1 + nota2) / 2
    print("\033[1;35m=+=" * 15)
    print(F"NA MATERIA {materia}")
    print("=+=" * 15)
    #Passo 3 mostrar seu resultado
        #Passo 3.1 Se a media for maior que 5 e menor que 7,mostre que está de recuperação
    if media > 5 and media < 7:
        print(f"\033[1;33mSua média foi {media:.2f} RECUPERAÇÃO! ESTUDE MAIS!")
        #PAsso 3.2 Senão se a media for menor ou igual a 5,mostre que reprovou
    elif media <= 5:
        print(f"\033[1;31mSua média foi {media:.2f} REPROVADO! ESTUDE MAIS!")
        #Passo 3.3 Senão se a media for maior ou igual a  7,mostre que está aprovado
    elif media >= 7:
        print(f"\033[1;34mSua média foi {media:.2f} PARABENS! FOI APROVADO,CONTINUE ASSIM!")
print("\033[1;97mPROGRAMA MEDIA FINALIZADO!")
