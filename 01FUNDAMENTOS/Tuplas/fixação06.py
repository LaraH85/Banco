#Escreva um programa que receba uma tupla com 10 números inteiros quaisquer.
# O programa deve gerar uma nova tupla contendo apenas os números pares da tupla original.

listas = (1,2,3,4,5,6,7,8,9,10)
numeros = ()

for i in listas:
    if i % 2 == 0:
        numeros += (i,)

print(numeros)

