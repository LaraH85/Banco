#Dada uma tupla misturada: itens = (10, "Python", 20, "Programação", 30, "Tuplas").
# Crie duas listas vazias. Percorra a tupla e, usando a função type(),
# coloque os números inteiros em uma lista e as strings na outra.
# No final, converta as duas listas de volta para tuplas e exiba-as.

itens = (10, "Python", 20, "Programação", 30, "Tuplas")

numeros_lista = []
strings_lista = []

for item in itens:
    if type(item) is int:
        numeros_lista.append(item)
    elif type(item) is str:
        strings_lista.append(item)

numeros_tupla = tuple(numeros_lista)
strings_tupla = tuple(strings_lista)

print("Tupla de inteiros:", numeros_tupla)
print("Tupla de strings:", strings_tupla)

