num = 0
contando = 0
soma = 0
while num != 999:
    num = int(input("Digite um numero inteiro: "))
    if num != 999:
        contando = contando + 1
        soma = soma + num
print(f"Você digitou {contando} numeros, a soma entre eles foi {soma}")
