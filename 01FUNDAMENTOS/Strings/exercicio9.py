#Faça um programa que leia um leia uma frase digitada pelo usuário e conte quantas palavras individuais existem
# nessa frase, mas exiba um relatório listando cada palavra em uma linha separada junto coma quantidade de letra
# que aquela palavra específica possui.

frase = input("Digite uma frase: ")

lista = frase.split()
frase = " ".join(lista)
contador = len(frase)
letras = [len(frase) for item in frase]

print(f"{contador}\n{frase}\n{letras}")