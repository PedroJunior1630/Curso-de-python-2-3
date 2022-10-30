print("\033[1;32m=+=" * 10)
print("TABUADA")
print("=+=" * 10)

numero = int(input("\033[1;97mDigite um numero inteiro: "))
escolha = int(input("Digite até qual tabuada você quer ver: "))

for tabuada in range(1,escolha + 1):
    print(f"\033[1;34m{numero} X {tabuada} = {numero * tabuada}")
