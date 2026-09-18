#13.(Controle de Acesso):
# Crie uma lista com 5 nomes de usuários cadastrados no banco de dados.
# Peça para o usuário digitar seu login e,
# utilizando o operador de pertinência (sem usar laços),
# exiba se ele possui acesso permitido
# ou se não foi encontrado.

print("=== CONTROLE DE ACESSO ===")

nomes = ["Helio", "Julio", "Lucas", "Maria", "Pedro"]

login = input("Informe o login: ")

for nome in nomes:
    if nome == login:
        print("Acesso pemitido!",nome in login)
    else:
        print("Usuario não encontrado!",nome in login)
