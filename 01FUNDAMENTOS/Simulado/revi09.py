#Questão 9 – Depuração de Código (1,0 ponto)
#Uma equipe de desenvolvimento identificou que um programa responsável pelo cálculo da média de avaliações não estava produzindo os resultados esperados.
#Após análise, verificou-se que o algoritmo utilizado era o seguinte:
#soma = 0 for nota in range(1,6): nota = float(input("Nota: ")) media = nota / 5 print(media)
#Analise cuidadosamente o algoritmo e responda:
#a) Qual é o erro lógico existente?
# O algoritmo possui dois erros lógicos principais:
#Cálculo da média fora do laço: A variável media está sendo calculada dentro do laço de repetição.
# Como o cálculo é nota / 5, o programa sobrescreve o valor da média a cada nova nota inserida, perdendo o histórico das anteriores.

#Ausência de acumulação: A variável soma foi criada, mas nunca é utilizada para somar as notas informadas pelo usuário.
# O valor da última nota digitada é o único considerado no cálculo final.

#b) Como esse erro afeta o resultado final?
#O resultado exibido no final será sempre a última nota digitada dividida por 5.
# O programa ignora completamente as quatro notas anteriores, impossibilitando o cálculo de uma média aritmética real,
# que deveria ser a soma de todas as notas dividida pela quantidade de avaliações

#c) Reescreva apenas as linhas necessárias para corrigir o algoritmo.
#Para corrigir, devemos acumular as notas na variável soma dentro do laço e realizar o cálculo da média apenas após o término do for.

soma = 0

for nota in range(1,6):
    valor_nota = float(input("Nota: "))

    soma = soma + valor_nota

media = soma / 5
print(f"A média é: {media}")