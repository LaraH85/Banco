#Peça para o usuário digitar uma senha.
# Se a senha for igual a "DevJunior2026", exiba "Senha Correta. Autenticando...".
# Caso contrário, exiba "Senha Incorreta. Acesso bloqueado!".

senha = input("Digite sua senha: ")

if senha == "DevJunior2026":
    print("Senha Correta. Autenticando...")

else:
    print("Senha Incorreta. Acesso bloqueado!")