'''Faça um programa que leia o horário de entrada (hora e minuto)
e o horário de saída (hora e minuto) de um empregado
e imprima quanto tempo, no formato hora:minuto, o empregado ficou na empresa.'''

hora_de_entrada = float(input("Digite a hora de entrada: "))
hora_de_saida = float(input("Digite a hora de saida: "))

produto = hora_de_saida - hora_de_entrada

print(f'A empregada ficou na empresa: {produto}H ')

