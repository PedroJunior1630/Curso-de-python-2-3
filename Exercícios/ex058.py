import random
computador = random.randint(1,10)
contando = 1

print("\033[1;34m=+=" * 20)
print("JOGO DA ADIVINHAÇÃO!")
print("=+=" * 20)

usuario = int(input("\033[1;32mTente adivinhar um número que estou pensando entre 1 e 10: "))

while usuario != computador:
    usuario = int(input("\033[1;31mOpa! não foi desta vez, Tente Novamente: "))
    contando = contando + 1

print("\033[1;33m=+=" * 20)
print(f"O computador pensou no número {computador}")
print("=+=" * 20)
print("\033[1;35m=+=" * 20)
print(f"Parabéns você conseguiu! Você tentou {contando} vezes até acertar")
print("=+=" * 20)
