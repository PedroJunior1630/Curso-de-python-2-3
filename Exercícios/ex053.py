frase = str(input("\033[1;97mDigite uma frase: ")).upper().strip()
for var in range(len(frase) -1 , -1, -1):

    frase2 = frase.replace(" ","")
    if frase2[var] == frase2:
        msg = "Palindromo"

    else:
        msg= "Não é um palindromo"
    print(frase2[var],end="")

print(f"\n\033[1;33m{msg}")