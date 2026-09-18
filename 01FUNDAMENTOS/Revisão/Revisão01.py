#Faça um programa que mostre todos os números de 1 a 100 e indique ao lado se o número é par ou ímpar.

for i in range(1,100):
    if i % 2 == 0:
        print(i)
        print("Número é par!")

    else:
        print(i)
        print("Número ímpar!")
