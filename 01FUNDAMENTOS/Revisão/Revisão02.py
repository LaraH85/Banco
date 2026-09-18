#Solicite um número ao usuário e exiba sua tabuada de 1 a 10.

num = int(input("Digite o para fazer a multiplicação de 1 a 10: "))

for i in range(1,11):
    resultado = num * i
    print(f'{i} x {num} = {resultado}')