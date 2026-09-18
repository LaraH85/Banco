#Um aplicativo de entrega precisa taxar pedidos.
#Pergunte se o pedido é feito em dia de semana ou final de semana.
#Se for final de semana, pergunte se está chovendo.
#Se estiver chovendo, adicione uma taxa extra de R$10.00.
#Se não estiver chovendo, a taxa é de apenas R$5.00.

pedidos = input("o pedido é feito em dia de semana ou final de semana:")

if pedidos == "final de semana":
    print("Final de semana!")
    pedidos = input("Está chovendo:")

    if pedidos == "Sim":
        print("Taxa extra de R$10.00")
    else:
        print("Taxa é de apenas R$5.00.")

else:
    print("O pedido foi feito em dia de semana!")

