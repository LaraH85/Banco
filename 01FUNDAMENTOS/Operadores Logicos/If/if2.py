#Crie um script que receba o saldo de uma conta bancária e o valor de uma compra.
# Se o valor da compra for maior que o saldo, exiba a mensagem: "Saldo insuficiente para esta transação!".

saldo = float(input("Digite seu saldo: "))
valor_da_compra = float(input("Digite seu valor da compra: "))

if valor_da_compra > saldo:
    print(f"Saldo insuficiente para esta transação R${valor_da_compra}!")

