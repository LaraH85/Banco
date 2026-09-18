#Crie um sistema de cadastro onde o usuário insere o nome da cidade de nascimento.
# O programa não pode aceitar respostas com menos de 3 caracteres.
# Force a digitação inicial usando a estrutura while True.


while True:
    print("Processando...")

    cidade = input("Digite seu cidade de nascimento: ")

    if len(cidade) > 3:
        print("Cidade aceita.")
        break
    else:
        print("Não aceita 3 caracteres.")