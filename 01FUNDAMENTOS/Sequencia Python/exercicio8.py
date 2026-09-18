'''Leia o preço de fábrica de um automóvel e exiba seu preço final.
Considere que o preço final é igual ao preço de fábrica mais o preço dos impostos (45% do preço de fábrica)
 mais a porcentagem do revendedor (28% do preço de fábrica)'''

fabrica = float(input("Digite o preço de fabrica: "))

imposto = fabrica * 0.45
revendedor = fabrica * 0.28
preco_final = fabrica + imposto + revendedor

print(f'Preço final: {preco_final:.2f} ')
