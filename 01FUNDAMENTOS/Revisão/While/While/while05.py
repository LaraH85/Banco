# Faça um programa que peça um nome de usuário e uma senha.
# A senha não pode ser igual ao nome do usuário.
# O sistema deve mostrar uma mensagem de erro
# e continuar pedindo as informações até que os dados sejam criados corretamente.

nome = input("Digite seu nome: ")
senha = input("Digite sua senha: ")

while senha == nome:
    print("Senha inválida!")
    senha = input("Digite seu senha: ")

    if senha != nome:
        break

print("Senha válida!")
