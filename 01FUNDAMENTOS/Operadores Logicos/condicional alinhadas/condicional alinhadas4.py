#Crie um validador de cupons de frete grátis.
# Primeiro veja se o valor total da compra é maior que R$100.
# Se for, pergunte o estado do cliente.
# Se o estado for "SP", o frete é grátis.
# Se não for de "SP", informe que o frete grátis não se aplica àquela região geográfica.

cupons = float(input("Valide seu cupon: "))

if cupons > 100:
    print("Aceito!")

    estado = input("Informe seu estado: ")
    if estado == "SP":
        print("Frete grátis!")
    else:
        print("o frete grátis não se aplica àquela região geográfica.")

else:
    print("Compre mais para conseguir frete gratis!")