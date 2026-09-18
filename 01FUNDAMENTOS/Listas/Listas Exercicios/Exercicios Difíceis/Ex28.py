#(Processamento de Dados): Uma lista contém strings com nomes de cidades em formatos variados:
# ["curitiba", "SÃO PAULO", "Curitiba", "Rio"].
# Faça um programa que peça uma busca do usuário e
# encontre as ocorrências ignorando maiúsculas e minúsculas.

listas = ["curitiba", "SÃO PAULO", "Curitiba", "Rio"]

cidade = input("Digite o nome da cidade: ") .strip() .lower()

resultado = []

for lista in listas:
    if lista.lower == cidade:
        print("Está na lista:",len(lista))
        resultado.append(lista)

    elif cidade in lista.lower():
        print("Está na lista:",lista)


