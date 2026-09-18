#Questão 7 – Interpretação de Algoritmo (1,0 ponto)
#Um desenvolvedor implementou o algoritmo abaixo para realizar uma contagem.
#contador = 0 for numero in range(10, 31): if numero % 3 == 0: contador += 1 print(contador)
#Sem executar o programa, responda:

#a) Qual valor será apresentado na tela? 7
#b) Explique detalhadamente como o algoritmo chegou a esse resultado:
#O algoritmo utiliza uma estrutura de repetição que percorre o intervalo de 10 a 30 (já que a função range(10, 31)
#inclui o início e exclui o limite final). Dentro desse laço, a condição if número % 3 == 0 verifica se o resto da divisão do número por 3 é igual a zero,
#ou seja, se o número é um múltiplo de 3.
#c) Caso fosse necessário contar os múltiplos de 5, qual linha do algoritmo deveria ser alterada?
#Alteração para múltiplos de 5
#Para contar os múltiplos de 5, a linha que deve ser alterada é a condição dentro do if.
# O divisor deve ser mudado de 3 para 5:
#Linha original: if numero % 3 == 0:
#Linha alterada: if numero % 5 == 0:
#Dessa forma, o programa passará a verificar quais números no intervalo de 10 a 30 possuem resto zero ao serem divididos por 5
# (neste caso, seriam os números 10, 15, 20, 25 e 30, resultando em uma contagem final de 5).

contador = 0

for numero in range(10,31):
    if numero % 3 == 0:
        contador += 1
print(f"O valor do contador:{contador}")