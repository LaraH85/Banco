#Um motorista quer saber se o dinheiro que ele tem é suficiente para encher o tanque.
#Peça o valor em dinheiro e o preço do tanque cheio.
#Se o dinheiro for suficiente, mostre "Abastecimento Autorizado!", senão mostre "Saldo insuficiente.".

saldo = float(input("Insira seu valor em dinheiro: R$ "))
tanque = float(input("Insira o preço do tanque cheio: R$ "))

if saldo >= tanque:
    valor = True
    print("Abastecimento Autorizado!")

else:
    valor = False
    print("Saldo insuficiente.")
