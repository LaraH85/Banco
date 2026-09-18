'''Faça um programa que leia o valor de uma mercadoria e
a porcentagem de desconto.
O programa deve imprimir o novo valor com desconto.'''

mercadoria = float(input("Digite o valor da mercadoria: "))
desconto = float(input("Digite o do desconto: "))


porcentagem = (mercadoria * desconto / 100)
subtracao = mercadoria - porcentagem

print(f' o valor do desconto: R${subtracao}')
