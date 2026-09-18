vendas = [100.0,250.50,50.0,300.0,80.0]

total_vendas = 0.0
vendas_altas = 0

#Passando por cada venda para somar e contar as maiorias que 100
for valor in vendas:
    total_vendas = total_vendas + valor
    if valor > 100.0:
        vendas_altas = vendas_altas + 1

#Calculando a quantidade de itens usando o len
quantidade = len(vendas)
media = total_vendas / quantidade

print("Total vendido: R$", total_vendas)
print("Média de vendas: R$", media)
print("Quantidade de vendas acima de R$100:", vendas_altas)