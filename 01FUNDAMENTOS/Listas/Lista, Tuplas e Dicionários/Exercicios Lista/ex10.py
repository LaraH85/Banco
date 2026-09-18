lista = []

for i in range(3):
    nome = input("Digite os nomes: ")

    lista.append(nome)

for i in lista:
    ordem_inversa = lista[::-1]
    ultimo_nome = lista[-1]

print(f"Ordem inversa: {ordem_inversa}")
print(f"O último nome: {ultimo_nome}")