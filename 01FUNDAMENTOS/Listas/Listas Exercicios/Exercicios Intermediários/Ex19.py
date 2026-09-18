#(Jogos): Uma lista armazena o inventário de um guerreiro:
# ["Espada", "Escudo", "Poção"]. O guerreiro usou sua "Poção".
# Use o método correto para apagar a poção da lista pelo nome e mostre o inventário atualizado.

jogos = ["Espada", "Escudo", "Poção"]
jogos.remove(jogos[2])
print('Inventario atualizado!')
print(jogos)