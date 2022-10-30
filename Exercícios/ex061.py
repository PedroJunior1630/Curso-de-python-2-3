print("\033[1;33m=+=" * 10)
print("PROGRESSÃO ARITIMÉTICA")
print("=+=" * 10)

a1 = int(input("\033[1;34mDigite o primeiro termo de uma P.A: "))
r = int(input("Digite a razão desta P.A: "))
an = a1 + (11 - 1) * r

while a1 < an:
    print(f"\033[1;35m{a1} >",end= " ")
    a1 = a1 + r
print("ACABOU!")
