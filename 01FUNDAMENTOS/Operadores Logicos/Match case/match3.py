#Crie um mini sistema de classificação de erros HTTP.
# O usuário insere o status code (ex: 200, 404, 500)
# e o programa diz se é "Sucesso",
# "Não Encontrado"
# ou "Erro de Servidor" usando match case.

code = input("o status code (ex: 200, 404, 500): ")

match code:
    case"200":
        print("200 Sucesso!")
    case"404":
        print("404 Não Encontrado!")
    case"500":
        print("500 Erro de Servidor!")

    case _:
        print("Status Code Invalido!")