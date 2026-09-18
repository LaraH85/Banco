#Simulador de Jogo de Futebol:
# Receba o nome e o número de gols de dois times
# e informe quem venceu ou se foi empate.

nome1 = input("Nome do time: ")
nome2 = input("Nome do time: ")
gols1 = int(input("Numero de gols: "))
gols2 = int(input("Numero de gols: "))

if gols1 < gols2:
    print(f"O time {nome2} venceu.")

elif gols1 == gols2:
    print(f"O time empatou.")

else:
    print(f"O time {nome1} ganhou.")
