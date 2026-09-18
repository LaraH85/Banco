#Aprovador de Financiamento de Carros:
# Peça o valor do carro,
# o salário do comprador
# e a quantidade de meses para pagar.
# Se o valor da parcela mensal ultrapassar 30% do salário,
# o financiamento deve ser "Negado".
# Caso contrário, "Aprovado".


carro = float(input('Digite o valor do carro: '))
salario = float(input('Digite o valor do salario: '))
meses = int(input('Digite a parcela em meses: '))

parcela = carro / meses
desconto_salario = salario * 0.30

if parcela > desconto_salario:
    print(f'Negado!')

else:
    print(f'Aprovado!')