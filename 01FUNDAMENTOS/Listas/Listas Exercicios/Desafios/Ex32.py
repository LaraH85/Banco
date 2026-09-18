#Desafio 2 (Ordenação de Ranking Manual):
# Uma máquina de fliperama possui uma lista desordenada com 6 pontuações de jogadores:
# [520, 1100, 250, 890, 1400, 600].
# Escreva um algoritmo usando laços de repetição aninhados (um laço dentro do outro) que ordene essa lista do maior para o menor valor,
# sem usar nenhuma função pronta de ordenação do Python.
# Mostre a lista ordenada.

pontos = [520, 1100, 250, 890, 1400, 600]

print(f"\nRanking original (desordenado): {pontos}")

n = len(pontos)

for i in range(n):
    for j in range(0,n - i - 1):

        if pontos[j] < pontos[j + 1]:

            auxiliar = pontos[j]
            pontos[j] = pontos[j + 1]
            pontos[j + 1] = auxiliar

print("-" * 50)
print(f"Ranking final (do maior para o menor): {pontos}")