#14.(E-commerce):
# Uma lista de preços de produtos contém [100, 200, 300, 400].
# O site entrou em promoção.
# Use um laço de repetição para atualizar cada gaveta da própria lista,
# aplicando um desconto de 10% sobre cada valor.


lista = [100, 200, 300, 400]
valor = 10

for item in lista:
    valor_desconto = (valor * (item / 100))
    preco_final = item - valor_desconto

    print("(10%) R$", preco_final)


