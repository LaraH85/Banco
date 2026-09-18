#25.(Almoxarifado):
# Uma lista de contagem de caixas possui valores positivos, nulos e negativos (erros de digitação):
# [15, -3, 0, 22, -1, 8].
# Construa um programa que conte e mostre quantos valores válidos (maiores que zero) existem na lista.

contador = 0

trabalhos = [15, -3, 0, 22, -1, 8]

for trabalho in trabalhos:
    if trabalho > 0:
        print("Números:",trabalho)
        contador += 1

print("\nValores maior que zero:",contador)




