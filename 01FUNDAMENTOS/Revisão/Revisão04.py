#Solicite a idade de 15 pessoas e informe:
#Quantos são maiores de idade;
#Quantos são menores de idade.

maior_idade = 0
menor_idade = 0

for idade in range(1,16):
    pessoas = float(input(f"Digite a idade {idade} pessoas: "))

    if pessoas > 18:
        maior_idade += 1

    else:
        menor_idade += 1
print(f"Maiores de idade: {maior_idade}")
print(f"Menores de idade: {menor_idade}")