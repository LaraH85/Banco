#Escreva um script que solicite o nome completo de um usuário.
# O loop de validação não deve aceitar nomes vazios (com zero caracteres) ou
# strings compostas apenas por espaços em branco.

nome = input("Digite o seu nome completo: ")

while len(nome) == 0:
    nome = input("Digite o seu nome completo: ")
    if len(nome) >= 1:
        break
    print("Colocar letras do seu nome!")