'''Leia um valor em dólar e o valor do câmbio (conversão de dólar para real). Calcule e exiba quantos reais equivalem ao valor lido em dólar.'''

dolar = float(input("Digite o valor em dolar: "))
cambio = float(input("Cambio(R$/Us$): "))

reais = dolar * cotacao

print(f"US$ {dolar:.2f} = R$ {reais:.2f}")