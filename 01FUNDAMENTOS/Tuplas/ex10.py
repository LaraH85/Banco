produtos = (
    ("Notebook", 3500),
    ("Mouse", 80),
    ("Monitor", 900),
    ("Keyboard", 150),
    ("Headset", 220)

)
notas = (3500, 80, 900, 150, 220)

numero = 0

for nome, preco in produtos:
    print(nome, preco)

    maior = max(notas)
    menor = min(notas)
    media = sum(notas) / len(notas)

print(f"\nProduto mais caro:R$ {maior}")
print(f"Produto mais barato:R$ {menor}")
print(f"\nMédia dos produtos:",media)

for i, notas in produtos:
    if notas > 500:
        numero += 1

print(f"Número acima de 500: {numero}")

