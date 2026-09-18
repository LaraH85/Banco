#Desenvolva um validador de planos de celular.
# O usuário digita o nome do plano ("Bronze", "Prata" ou "Ouro")
# e o sistema mostra a quantidade de internet incluída (10GB, 50GB ou Ilimitado).

plano = input("Informe o plano do seu celular: ")

match plano:
    case "Bronze":
        print("10GB")
    case "Prata":
        print("50MB")
    case "Ouro":
        print("Ilimitado!")
