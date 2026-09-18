produtos = {}

for i in range(5):
    nome = input('Cadastre os produtos: ')
    preco = float(input('Digite o preço: R$'))
    produtos[nome] = preco

print('\nProdutos - Preço:')
for nome, preco in produtos.items():
    print(f'{nome} - {preco:.2f}')