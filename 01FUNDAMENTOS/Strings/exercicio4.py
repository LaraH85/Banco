#Uma URL do sistema está estruturada assim:
# [loja.com/produto/categoria/games/ps5](https://loja.com/produtos/categorias/games/ps5).
# Crie um script que extraia apenas a palavra "games" e "ps5" dessa string utilizando fatiamento ou métodos da divisão.

frase = "[loja.com/produto/categoria/games/ps5](https://loja.com/produtos/categorias/games/ps5)"

termo1 = frase[-10:]
termo2 = frase[76:]

print(termo1)
print(termo2)
