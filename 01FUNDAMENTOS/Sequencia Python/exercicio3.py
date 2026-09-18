'''Leia uma temperatura em Fahrenheit e exiba o equivalente em
Celsius. A fórmula de conversão é:'''

# C = 5/9 (F - 32)

num1 = float(input("Digite um produto em Fahrenheit: "))

Fahrenheit  = num1 - 32
produto = Fahrenheit * 5
divisao = produto / 9

print(f'A subtração de {num1} e {32} é: {Fahrenheit}')
print(f'A produto de {Fahrenheit} e {5} é: {produto}')
print(f'A divisão de {produto} e {9} é: {divisao}')