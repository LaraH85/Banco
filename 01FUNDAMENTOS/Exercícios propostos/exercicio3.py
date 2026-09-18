'''Faça um programa que leia 2 números inteiros da entrada e imprima o resto da divisão inteira de um pelo outro.'''

num1 = float(input("Digite um número: "))
num2 = float(input("Digite outro número: "))

divisao = num1 / num2
mod = num1 % num2

print(f'A resto da divisão é: {mod} \n')