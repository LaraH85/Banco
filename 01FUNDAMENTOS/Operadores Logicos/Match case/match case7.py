#Verificador de Vogal ou Consoante:
# Faça um script que leia uma única letra do teclado e determine se ela é uma vogal ou uma consoante.

vogal = input("Digite consoante ou vogal: ")

if vogal in "aeiou":
    print(f'A letra: {vogal} vogal')

else:
    print(f'A letra é uma consoante!')
