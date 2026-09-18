
num1 = float(input("Digite um número; "))
num2 = float(input("Digite um numero: "))
num3 = float(input("Digite um numero: "))
num4 = float(input("Digite um numero: "))

# Aritiméticos
soma = num1 + num2
subtracao = num1 - num2
produto = num1 * num2
divisao = num1 / num2
mod = num1 % num2
porcentagem = num1 ** num2

print(f'A soma de {num1} e {num2} é: {soma} ')
print(f'A subtração de {num1} e {num2} é: {subtracao} ')
print(f'A produto de {num1} e {num2} é: {produto} ')
print(f'A divisão de {num1} e {num2} é: {divisao} ')
print(f'A resto da divisão {num1} e {num2} é: {mod} ')
print(f'A porcentagem de {num1} e {num2} é: {porcentagem} ')

# Comparação

maior = num1 > num2
menor = num1 < num2
igual = num1 == num2
diferente = num1 != num2
maior_igual = num1 >= num2
menor_igual = num1 <= num2

print(f'o numero {num1} é maior que o numero {num2}: {maior}')
print(f'o numero {num1} é menor que o numero {num2}: {menor}')
print(f'o numero {num1} e o numero {num2} são iguais: {igual}')
print(f'o numero {num1} e o numero {num2} saõ diferente: {diferente}')
print(f'o numero {num1} é maior ou igual que numero {num2}: {maior_igual}')
print(f'o numero {num1} é menor ou igual que numero {num2}: {menor_igual}')

# Atribuição

num1 += 1 # é igual a num1 = num1 + 1
num2 -= 1 # é igual a num2 = num2 - 1
num3 *= 1 # é igual a num3 = num3 * 1
num4 /= 1 # é igual a num4 = num4 / 1

print(num1)
print(num2)
print(num3)
print(num4)

