#Crie um programa que peça uma senha e continue solicitando até que a senha correta seja digitada.

senha = ""

while senha != "senac123":
    senha = input("Digite uma senha: ")

    if senha == "senac123":
        print("Senha correta!")
        break
    else:
        print("Senha incorreta!")

print(f"Senha correta: {senha}")