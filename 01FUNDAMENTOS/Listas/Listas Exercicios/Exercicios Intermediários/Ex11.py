#11.(Supermercado):
# Dada a lista de preços [12.50, 4.99, 35.00, 8.20, 120.00],
# crie um programa que utilize a função embutida do Python para calcular e
# mostrar o valor total da compra.

print("===SUPERMERCADO===")

precos = [12.50, 4.99, 35.00, 8.20, 120.00]

total_compras = 0.0

for valor in precos:
    total_compras = total_compras + valor

print("Valor total da compra:", total_compras)