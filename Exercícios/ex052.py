numero = int(input("Digite um número: "))
qntd = 0

for var in range(1,numero + 1):

    if numero % var == 0:
        print("\033[1;34m",end=" ")
        qntd = qntd + 1
    else:
        print("\033[1;31m",end=" ")

    if qntd == 2:
        msg = "Este número é primo"
    else:
        msg = "Este número não é primo"

    print(var,end=" ")

print(f"\n\033[1;33mEste número foi divisivel {qntd} vezes")
print(f"\033[1;33m{msg}")
