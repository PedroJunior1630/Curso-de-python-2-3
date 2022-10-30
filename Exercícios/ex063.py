numero = int(input("Digite um número inteiro: ")) 
termo1 = 0
termo2 = 1
contador = 3
print(f"{termo1} > {termo2} > ",end= " ")
while contador <= numero:
    termo3 = termo1 + termo2
    print(termo3," > ",end= " ")
    termo1 = termo2
    termo2 = termo3
    contador = contador + 1
print("ACABOU!")
