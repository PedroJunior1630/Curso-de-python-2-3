num = 1
soma = 0
contador = 0
maior = 0
menor = 0

while num > 0:
    num = int(input("Digite um número inteiro: "))
    
    if num > 0:
        soma = soma + num
        contador = contador + 1

        if contador == 1:
           maior = num
           menor = num

        else:
            if num > maior:
                maior = num

            if num < menor:
                menor = num

print(f"A média desses valores são: {soma / contador}")
print(f"O maior valor digitado: {maior}")
print(f"O menor valor digitado: {menor}")
