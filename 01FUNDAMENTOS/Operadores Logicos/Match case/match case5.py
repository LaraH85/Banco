#Autenticação em Dois Fatores (2FA):
# Crie um script que receba a senha do usuário.
# Se estiver certa,
# peça um código token de 6 dígitos enviado por SMS (simule o token correto fixo no código como 123456).
# Valide o fluxo completo.

senha = input("Digite seu senha: ")

if senha == "123456":
    print("Senha correta!")
else:
    print("Senha incorreta!")
