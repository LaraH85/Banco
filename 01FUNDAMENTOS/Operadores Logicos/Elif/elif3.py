#Desenvolva uma calculadora de desconto baseada na forma de pagamento:
# Opção 1 - Dinheiro (15% de desconto),
# Opção 2 - Cartão de Crédito (Preço Normal),
# Opção 3 - Pix (10% de desconto).
# Qualquer outra entrada deve exibir "Opção inválida".

valor = float(input("Digite o valor: \n"))
forma_de_pagamento = input("Digite o forma de pagamento:\n")

tipo_pagamento = "Dinheiro", "Cartão", "Pix"
valor = valor

if forma_de_pagamento == "Dinheiro":
    desconto = 0.15
elif forma_de_pagamento == "Cartão":
    desconto = 0.0
elif forma_de_pagamento == "Pix":
    desconto = 0.10
else:
    desconto = 0.0
    print("Opção inválida.")

valor_final = valor - (valor * desconto)
print(f"Pagamento {forma_de_pagamento} recebe {desconto*100}% de desconto")
print(f'Valor final R${valor_final:.2f}')