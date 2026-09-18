print('--- Digite 12 numeros ---')

numeros = []

for i in range(5):
    num = int(input('Digite um numero: '))
    numeros.append(num)

positivo = [i for i in numeros if i >= 0]
negativo = [i for i in numeros if i < 0]

print(f'\nNumeros: {numeros}')
print(f'Positivos: {positivo}')
print(f'Negativos: {negativo}')