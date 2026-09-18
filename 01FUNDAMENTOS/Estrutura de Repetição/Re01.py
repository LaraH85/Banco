# Faça um programa que peça uma nota, entre zero e dez.
# Mostre uma mensagem caso o valor seja inválido e
# continue pedindo até que o usuário informe um valor válido.

numero = 0

while numero < 1 or numero > 10:
    pergunta = float(input("Digite sua nota: "))

    if 0 <= pergunta <= 10:
        print("Valor Válido!")
        break

    else:
        print("Inválido!")