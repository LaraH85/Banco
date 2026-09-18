#Escreva um código que receba uma senha do usuário.
# Se a senha for "senha123", imprima "Acesso liberado".
# Se falhar, exiba a mensagem "Senha incorreta, tente outra vez" e reinicie o pedido imediatamente usando o modelo de loop while True.

while True:

    senha = str(input("Escreva sua senha: "))

    if senha != "senha123":
        print("Senha incorreta, tente novamente.")

    if senha == "senha123":
        print("Acesso liberado!")
        break