'''Crie um sistema de validação de login. O acesso só deve ser concedido (True) se o usuário for igual a "admin" e a senha for igual a "12345".'''

usuario = "admin"
senha_salva = "12345"


print(usuario == "admin" and senha_salva == "12345") # Saída: True
print(usuario == "admin" and senha_salva == "errado") # Saída: False