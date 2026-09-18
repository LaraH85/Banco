#Concatenando com Python
'''
Jogoteca
'''
name = input("Digite o nome do jogo: \n")
yearLaunch = int(input("Digite o ano de lançamento do jogo: \n"))
gamePrice = float(input("Digite o preço do jogo: \n"))
planInclude = (input("Plano Incluso: \n"))

#Alternativa 1

print("Nome do Jogo: \n", name)
print("Ano do Jogo: \n", yearLaunch)
print("Preço do Jogo: \n", gamePrice)
print("Plano Incluso: \n", planInclude)

#Alternative 2

print("Nome do Jogo:", name, "\nAno de Lançamento:", yearLaunch,
      "\nPreço do Jogo: ", gamePrice, "\nPlano Incluso: ", planInclude)

#Alernative 3

print(f"O nome do jogo é: {name}. \nO preço do jogo é: {gamePrice}. \nO ano do jogo é: {yearLaunch}, \nPlano incluso: {planInclude}")
