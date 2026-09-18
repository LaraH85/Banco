'''Faça um programa que leia dois valores inteiros representando, respectivamente,
um valor de hora e um de minutos e
informe quantos minutos se passaram deste o início do dia.
Exemplo:
valores lidos  13 15
impressão  795 minutos'''

num1 = float(input("Digite a hora: "))
num2 = float(input("Digite os minutos: "))

produto = num1 * 60 + num2

print(f'Desde o início do dia se passou: {produto} ')



