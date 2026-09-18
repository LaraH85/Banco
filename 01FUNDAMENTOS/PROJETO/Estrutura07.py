#Escreva um programa que fique pedindo para o usuário digitar um número.
#O programa só deve parar de pedir quando o usuário digitar exatamente o número 0.

senha = ""

while senha != "0":
    senha = input("Digite a senha secreta: ")
    print("Acesso liberado!")