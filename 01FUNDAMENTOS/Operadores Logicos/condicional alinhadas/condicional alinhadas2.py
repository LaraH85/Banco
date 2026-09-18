#Faça um programa que leia o login de um usuário.
# Se o login for válido, peça a senha.
# Se a senha também for correta, dê as boas-vindas.
# Mostre erros específicos para cada etapa caso o usuário falhe.

login = input("Digite seu login: ")

if login == "megaBlaster":
    print("Aceito!")
    senha = input("Informe sua senha: ")

    if senha == "123456":
        print("Boas-Vindas!")
    else:
        print("Senha incorreta!")
else:
    print("Login incorreto! Tente novamente.")