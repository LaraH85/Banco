#Conversor de Moedas Dinâmico:
# Crie um menu onde o usuário escolhe a moeda de destino para converter $R\$\,100.00$: 1-Dólar, 2-Euro, 3-Libra.
# Faça o cálculo e
# imprima o valor convertido usando a estrutura estudada.

real = int(input("Digite quanto tem: R$ "))
cotacao = float(input("Digite a cotação diária: "))
moedas = input("Digite o tipo de moeda:")

if moedas == "Dólar":
    Dólar = cotacao * real
    print(f"US$ {Dólar:.2f} ")
elif moedas == "Euro":
    Euro = cotacao * real
    print(f"€$ {Euro:.2f} ")
elif moedas == "Libra":
    Libra = cotacao * real
    print(f"£$ {Libra:.2f} ")

else:
    print("Algo deu errado, tente novamente.")