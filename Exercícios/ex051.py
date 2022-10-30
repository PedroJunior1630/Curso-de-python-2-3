print("\033[1;33m=+=" * 15)
print("Vendos os próximos termos de uma P.A")
print("=+=" * 15)

a1 = int(input("\033[1;97mDigite o primeiro termo: "))
r = int(input("Digite a razão: "))
n = int(input("Digite quantos termos a seguir deseja ver: "))
an = a1 + ((n + 1) - 1) * r

for var in range(a1,an,r):
    print(f"\033[1;34m{var} >",end=" ")
print("ACABOU")
