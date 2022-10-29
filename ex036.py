#Passo 1 perguntar o valor da casa,do salario do comprador e quantos anos irá pagar
casa = int(input("Digite o valor da casa R$: "))
salario = int(input("Digite o salário do comprador R$: "))
anos = int(input("Digite em quantos anos pretende pagar: "))
#Passo 2 Calcular as prestações
meses = anos * 12
prestacao = casa / meses
#Passo 3 Calcular 30% do salario
salario30 = salario * 30 / 100
#Passo 4 Se as prestações foram menor ou igual a 30% do salario aprove
if prestacao <= salario30:
    print(f"\033[1;32mEMPRÉSTIMO APROVADO! serão {meses} prestações de R${prestacao:.2f}")
#Passo 5 Senão não aprove
else:
    print(f"\033[1;31mEMPRÉSTIMO NEGADO! ultrapassou o limite de 30% de seu salário sendo parcelas de {prestacao:.2f}")
