#Crie um programa que funcione como um simulador simples de poupança:
# pergunte o valor inicial investido,
# o rendimento mensal fixo em porcentagem (ex: 1%) e
# exiba quanto dinheiro estará na conta mês a mês durante o primeiro ano (12 meses).
import time
print("Comece seu investimento!")
time.sleep(1)


notas_para_inserir = float(input("Valor inicial investimento: "))
porcentagem = float(input("Valor porcentagem investimento (%): "))

taxa_decimal = porcentagem / 100

mes = 1

while mes <= 12:

    notas_para_inserir += notas_para_inserir * taxa_decimal


    print(f"Mês {mes:02d}: R$ {notas_para_inserir:.2f}")


    mes += 1

print(f"Simulação concluída! Saldo final após 1 ano: R$ {notas_para_inserir:.2f}")