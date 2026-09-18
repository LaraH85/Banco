#Crie um script validador de senhas fortes. Para a senha ser considerada válida, ela precisa atender
#cumulativamente a três regras:
#Ter pelo menos 8 caracteres de tamanho.
#Conter pelo menos um número.
#Conter pelo menos uma letra.

senha = str(input("Digite sua senha: "))
letras = 0
numeros = 0

for caracter in senha:
    if caracter.isalpha():
        letras += 1
    if caracter.isdigit():
        numeros += 1
    if len(senha) >= 8 and letras >= 1 and numeros >= 1:
        print("Autorizada com sucesso!")
        break

else:
    print("Senha invalida.")
