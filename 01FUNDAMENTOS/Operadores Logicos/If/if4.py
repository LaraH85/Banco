#Desenvolva um script que receba o preço de um produto.
#Se for maior que $R\$\,500.00$, exiba na tela: "Produto elegível para parcelamento sem juros!".

preco = float(input("Preço do produto: R$"))

if preco > 500:
    print("Produto elegível para parcelamento sem juros!")