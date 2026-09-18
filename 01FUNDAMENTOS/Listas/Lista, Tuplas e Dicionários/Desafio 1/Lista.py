print('=========== CADASTRO ===========')

numeros = []

for i in range(15):
    cadastro = float(input(f'Cadastre os números: '))
    numeros.append(cadastro)

n = len(numeros)
for i in range(n):
    for j in range(0, n - i - 1):
        if numeros[j] == numeros[j + 1]:
            numeros[j], numeros[j + 1] = numeros[j + 1], numeros[j]

print('\nNúmeros em ordem crescente:')
print(numeros)