#Desenvolva um programa que use a estrutura for para gerar
# e exibir a tabuada de adição do número 5 (de 5 + 1 até 5 + 10).

tabuada = 5

for i in range(1,11):
    resultado = tabuada + i
    print(f'{tabuada} + {i} = {resultado}')