'''Faça um programa que leia um valor representando o gasto realizado por um cliente do restaurante COMABEM e
imprima o valor total a ser pago, considerando os 10% do garçom.'''

gasto = float(input("Digite o valor: "))

gorjeta = gasto / 10
mod = gasto + gorjeta

print(f'O vcalor total é: {mod} \n')