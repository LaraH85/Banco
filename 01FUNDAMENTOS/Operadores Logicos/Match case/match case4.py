#Validador de Data de Vencimento:
# Receba o dia atual e o dia de vencimento de um boleto.
# Se o dia atual for maior que o vencimento, exiba "Boleto Vencido! Juros de atraso aplicados."
# , caso contrário "Boleto em dia.
# Pode pagar normalmente.".

dia = int(input("Digite o dia atual:"))
data = int(input("Digite o dia de Vencimento: "))

if dia > data:
    print("Boleto Vencido! Juros de atraso aplicados.")

else:
    print("Boleto em dia.")
    print("Pode pagar normalmente.")