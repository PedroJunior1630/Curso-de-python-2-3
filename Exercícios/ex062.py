
a1 = int(input("Digite o primeiro termo: "))
r = int(input("Digite a razão: "))
contador = 0
termos = 10
while contador < termos: 
    print(a1,end= " ")
    a1 = a1 + r
    contador = contador + 1
    if contador == termos:
        termo = int(input("\nDeseja ver mais alguns termos? (0 para não): "))
        if termo == 0:
            break
        else:
            termos = termos + termo
print("PROGRAMA FINALIZADO COM SUCESSO")
