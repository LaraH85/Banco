#Crie uma tupla com 5 números inteiros digitados pelo usuário (use um loop para ler).
# Depois, exiba:
#O maior número.
#O menor número.
#A soma de todos os valores.

contador = 0

numeros = []

while contador < 5:
    pergunta = float(input("Digite os numeros inteiros: "))
    contador += 1

    numeros.append(pergunta)
tupla = tuple(numeros)

print(max(tupla))
print(min(tupla))
print(sum(tupla))



