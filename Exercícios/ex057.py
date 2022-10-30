#sexo = str(input("Digite seu sexo: [F/M]: ")).strip().upper()
#while sexo != "M" and sexo != "F":
#   sexo = str(input("OPÇÃO INVALIDA! Digite novamente[F/M]: "))


sexo = str(input("Digite seu sexo: [F/M]: ")).strip().upper()[0]
if sexo[0] != "M" or sexo[0] != "F":
    while True:
        sexo = str(input("OPÇÃO INVALIDA! Digite novamente[F/M]: ")).strip().upper()[0]
        if sexo[0] == "M" or sexo[0] == "F":
            break
print(F"SEXO {sexo} REGISTRADO COM SUCESSO!")   
