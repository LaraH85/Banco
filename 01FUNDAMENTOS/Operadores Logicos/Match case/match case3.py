#Cálculo de Imposto Progressivo:
# Peça o salário de um desenvolvedor júnior.
# Se for maior que R$4000.00 exiba o desconto de 27.5% de imposto.
# Se for entre R$2500.00 e R$4000.00, aplique 15%.
# Abaixo disso, exiba "Isento".

imposto = float(input("Digite seu salário: "))

if imposto > 4000:
    desconto = 0.275

elif imposto >= 2500:
    desconto = 0.15

else:
    desconto = 0.0
    print("Isento!")

valor_final = imposto - (imposto * desconto)
print(f"Pagamento R${imposto} recebe {desconto * 100}% de desconto")
print(f'Valor final R${valor_final:.2f}')

