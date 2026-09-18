#3.Peça 10 números ao usuário e informe:
#Quantos são positivos;
#Quantos são negativos;
#Quantos são iguais a zero.

total_positivo = 0
total_negativo = 0
total_0 = 0

print("Coloque se o numero que é positivo, negativo ou 0!")

for pergunta in range(1,11):
    pergunta_numero = float(input(f"Informe {pergunta}º numero: "))

    if pergunta_numero > 0:
        total_positivo += 1

    elif pergunta_numero < 0:
        total_negativo += 1

    else:
        total_0 += 1

print(f"Total de positivos: {total_positivo}")
print(f"Total de negativos: {total_negativo}")
print(f"Total de 0: {total_0}")
