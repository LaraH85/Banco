#Receba uma frase do usuário, converta as palavras dessa frase em uma tupla e
# exiba os elementos dessa tupla na ordem inversa (do último para o primeiro).

frase = input("Digite algo: ")

coisas = tuple(frase)
palavra = tuple(frase[::-1])

print(coisas)
print(palavra)

