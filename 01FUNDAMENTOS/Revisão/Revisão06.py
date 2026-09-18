#Solicite 10 números e informe o maior e o menor valor digitado.

maior_numero = None
menor_numero = None

for nota in range(1,10):
    pergunta = int(input("Digite o número para saber qual é o maior e menor: "))

    if maior_numero is None or pergunta > maior_numero:
        maior_numero = pergunta
    if menor_numero is None or pergunta < menor_numero:
        menor_numero = pergunta


print(f"maior numero é {maior_numero}")
print(f"menor numero {menor_numero}")