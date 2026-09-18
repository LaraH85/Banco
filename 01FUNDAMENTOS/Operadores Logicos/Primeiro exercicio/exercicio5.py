#Para um produto ser enviado com frete grátis, o valor total deve ser maior que $R\$\,150.00$ ou o cliente deve possuir uma assinatura Prime.
#Peça esses dados e exiba o resultado lógico.

carrinho = float(input("Digite a quantidade no carrinho: "))
assinatura_prime = input("Digite se tem assinatura ou não: ")

if carrinho > 150.00 or assinatura_prime == "assinatura":
    compra = True
    print(f'Você ganhou frete grátis!')

else:
    print(f'Faça mais compras para ganhar frete grátis!')




