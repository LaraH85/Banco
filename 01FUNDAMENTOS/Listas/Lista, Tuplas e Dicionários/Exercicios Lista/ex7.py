listas = []
pares = 0
impares = 0

for i in range(5):
    pergunta = int(input('Digite um número: '))

    listas.append(pergunta)

for lista in listas:
    if lista % 2 == 0:
        pares += 1
    else:
        impares += 1

    print(lista)
    print(len(listas))