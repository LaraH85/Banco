#Questão 1 – Tarifa de Energia Elétrica (1,0 ponto)

#Nos últimos anos, o aumento do consumo de energia elétrica levou diversas concessionárias a adotarem mecanismos para incentivar o uso consciente dos recursos energéticos.
# Em uma dessas concessionárias, o valor da conta é calculado com base no consumo mensal do cliente,
# podendo haver cobrança de uma taxa adicional para consumidores que ultrapassam determinado limite de consumo.
#Considere as seguintes regras:

#Valor do kWh: R$ 0,85;
#Caso o consumo seja superior a 250 kWh, acrescentar uma taxa fixa de R$ 30,00.
#Desenvolva um programa que receba o consumo mensal de um cliente e apresente:
#Consumo informado;
#Valor total da conta.

print("===Tarifa de Energia Elétrica===\n")
print("Valor do kWh: R$0,85\n")

valor = 0.85
limite_consumido = 250.0
taxa_adicional = 30.00
consumo = float(input("Digite o seu consumo mensal: "))

if consumo < 0:
    print("Tente novamente!O consumo esta negativo.")

elif consumo > limite_consumido:
    total = consumo * valor
    Valortotal = total + taxa_adicional

    print("\n---Resumo da Conta---")
    print(f"Consumo informado pelo cliente: {consumo:.2f} kWh")
    print(f"Valor da conta: R$ {Valortotal:.2f}")

else:
    print("Erro no programa...")
