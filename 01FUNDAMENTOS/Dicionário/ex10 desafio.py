produtos = []

print("--- MINI SISTEMA DE CADASTRO ---")

while True:
    nome = input("\nNome do produto (ou 'sair' para encerrar): ").strip()
    if nome.lower() == 'sair':
        break

    try:
        preco = float(input(f"Preço de '{nome}': R$ "))
        estoque = int(input(f"Quantidade em estoque de '{nome}': "))
    except ValueError:
        print("Erro: Digite valores numéricos válidos para preço e estoque.")
        continue

    produto = {
        "nome": nome,
        "preco": preco,
        "estoque": estoque
    }

    produtos.append(produto)
    print(f"Produto '{nome}' cadastrado com sucesso!")

if len(produtos) > 0:

    print("\n" + "=" * 30)
    print("      PRODUTOS CADASTRADOS      ")
    print("=" * 30)
    for p in produtos:
        print(f"Nome: {p['nome']} | Preço: R$ {p['preco']:.2f} | Estoque: {p['estoque']}")

    print("\n" + "=" * 30)
    print("           RELATÓRIOS           ")
    print("=" * 30)

    produto_mais_caro = max(produtos, key=lambda x: x['preco'])
    print(f"• Produto mais caro: {produto_mais_caro['nome']} (R$ {produto_mais_caro['preco']:.2f})")

    valor_total_estoque = sum(p['preco'] * p['estoque'] for p in produtos)
    print(f"• Valor total do estoque: R$ {valor_total_estoque:.2f}")

    print(f"• Quantidade de produtos cadastrados: {len(produtos)}")
    print("=" * 30)

else:
    print("\nNenhum produto foi cadastrado.")
