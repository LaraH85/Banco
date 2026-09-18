'''Um parque de diversões tem uma montanha-russa radical.
Para andar nela, a pessoa deve ter altura maior que 1.60m OU idade maior que 14 anos.
Escreva a expressão lógica que valida a entrada.'''

idade = int(input("Digite sua idade: "))
altura = float(input("Digite sua altura: "))

if idade > 14:
    pode_andar_na_montanha = True

if altura > 1.60:
    pode_andar_na_montanha = True

print(idade > 14 or altura > 1.60)