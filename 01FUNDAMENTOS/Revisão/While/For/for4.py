#Dada a lista de nomes de linguagens de programação ["Python", "JavaScript", "C#", "PHP"],
# utilize a estrutura de repetição com enumerate() para exibir as linguagens no formato de lista enumerada:
# "1 - Python", "2 - JavaScript", etc.

lista = ["1 - Python", "2 - JavaScript", "3 - C#", "4 - PHP"]


for indice_linha, linha in enumerate(lista):
    print(f"Elemento = {linha}")
