#Crie um script para um pet shop.
# O usuário digita o tipo de animal ("cachorro", "gato", "pássaro", "peixe")
# e o sistema retorna a recomendação de corredor de ração específica usando o match case.

pet = input("Digite o nome do pet  (cachorro, gato, pássaro, peixe): ")

match pet:
    case "Cachorro":
        print("O corredor 1 se encontra o cachorro!")
    case "Gato":
        print("O corredor 2 se emcontra o gato!")
    case "Pássaro":
        print("O corredor 3 se encontra o pássaro!")
    case "Peixe":
        print("O corredor 4 se encontra o peixe!")
