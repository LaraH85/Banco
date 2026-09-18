#Escreva um programa que peça para o usuário digitar 5 números (um de cada vez).
# Ao final, o programa deve exibir a soma total desses 5 números.

cont1 = int(input("Digite o numero:"))
cont2 = int(input("Digite o numero:"))
cont3 = int(input("Digite o numero:"))
cont4 = int(input("Digite o numero:"))
cont5 = int(input("Digite o numero:"))

for cont in range(1):
    soma = cont1 + cont2 + cont3 + cont4 + cont5
    print(f"{soma}")