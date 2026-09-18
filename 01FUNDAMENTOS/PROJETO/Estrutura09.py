#Escreva um algoritmo que peça uma nota ou número para o usuário.
# Se o número digitado for negativo,
# peça para ele digitar novamente,
# repetindo até que ele digite um número positivo ou zero.

senha = int(input('Digite sua senha: '))

while senha < 0:
    senha = int(input("Digite uma senha: "))
   