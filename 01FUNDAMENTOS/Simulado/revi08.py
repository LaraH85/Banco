#Questão 8 – Análise de Algoritmo (1,0 ponto)
#Durante uma revisão de código, um analista encontrou o seguinte trecho de programa.
#soma = 0 for numero in range(1, 11): if numero % 2 == 0: soma += numero print(soma)
#Com base no algoritmo apresentado, responda:

#a) Qual será a saída produzida?
#30

#b) Explique o papel da estrutura condicional existente dentro do laço de repetição.
#Dentro do laço de repetição for, que percorre os números de 1 a 10,
# a estrutura condicional if numero % 2 == 0 atua como um filtro.

#c) Caso o objetivo fosse somar apenas os números ímpares, qual alteração deveria ser realizada?
#A alteração para somar números ímpares. Para somar apenas os números ímpares, você deve alterar a condição do if.
# Em vez de verificar se o resto é igual a zero, deve-se verificar se o resto é igual a 1 (ou diferente de zero).
#Linha original: if numero % 2 == 0:
#Linha alterada: if numero % 2 != 0: (ou if numero % 2 == 1:)

soma = 0

for numero in range(1, 11):
    if numero % 2 != 0:
        soma = soma + numero

print(f"Soma de numero de ímpares: {soma}.")
