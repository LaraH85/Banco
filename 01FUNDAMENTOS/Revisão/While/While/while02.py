#Desenvolva um sistema básico que leia números inteiros fornecidos pelo usuário e
# conte quantos números digitados eram pares.
# O loop encerra quando o usuário digitar o número 0.

num = float(input("Escreve números inteiros: "))

while num != 0:
    num = float(input("Escreve números inteiros: "))

    if num % 2 == 0:
        print("Numero par!")

    else:
        print(f"NUmero impar!")

    if num == 0:
        break

