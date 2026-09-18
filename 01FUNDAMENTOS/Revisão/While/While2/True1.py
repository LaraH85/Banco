#Crie um script que peça a digitação de um número positivo e exiba o seu quadrado.
# O loop deve perguntar ao final se o usuário deseja efetuar o cálculo para outro número.
# Garanta que o cálculo seja feito pelo menos uma vez antes da pergunta.

while True:
    print("Digite um numero positivo!")

    numero = int(input("Digite o numero: "))

    if numero > 0:
        calculo = numero ** 2
        resultado = calculo
        print(calculo)
    break
