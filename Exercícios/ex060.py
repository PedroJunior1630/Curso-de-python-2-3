'''numero = int(input("Digite um número inteiro: "))
import math 
print(F"A fatorial deste número é {math.factorial(numero)}")'''

numero = int(input("Digite um número: "))
fator = 1

print(f"{numero} != ",end= " ")

while numero > 0:
    print(numero,end= " ")
    print("x" if numero > 1 else "=",end= " ")
    fator = fator * numero
    numero = numero - 1

print(fator)
