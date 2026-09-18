#Crie uma tupla contendo 6 nomes de produtos de um supermercado.
# Peça para o usuário digitar o nome de um produto.
# Se o produto estiver na tupla, mostre em qual posição (índice) ele está.
# Caso contrário, exiba uma mensagem dizendo que o produto não foi encontrado.

compras = ("Sabonete", "Colgate", "Carne", "Frutas", "Verduras", "Frango")

produto = input("Digite o nome do produto: ")

if produto in compras:
    print("Posição na lista:",compras.index(produto))
else:
    print("Produto não encontrado.")

