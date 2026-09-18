# 15.(Biblioteca):
# Crie uma lista de livros.
# Use um laço de repetição para percorrer a lista
# e contar quantos livros possuem o título exato de "Python Básico".

livros = ["O Pequeno Principe","Cem Anos de Solidão","Python Básico","Python Básico", "Quem é você Alasca?"]
livros_python = 0

for livro in livros:
    if livro == "Python Básico":
        livros_python += 1

print("===  QUANTIDADE DE LIVROS ===")
print("Quantidade de livros Python Básico:",livros_python)