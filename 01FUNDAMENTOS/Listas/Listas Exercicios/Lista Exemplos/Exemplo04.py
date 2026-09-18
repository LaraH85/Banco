
filmes = ["Batman", "Super-Homem", "Coringa"]

#len(filmes) vai nos dar o número 3, que é a quantidade de itens
tamanho = len(filmes)

#Usando o while para navegar pelos índices de 0 até 2
indice = 0
while indice < tamanho:
    print("Filme da posição", indice, "é:", filmes[indice])
    indice = indice + 1 #Avança para a prócimo índice