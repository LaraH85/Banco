# Exemplo Praticos: Sistema de Login

usuario_salvo = "admin"
senha_salva = "1234"

#Ambas as condições precisam ser verdadeiras
print(usuario_salvo == "admin" and senha_salva == "1234") # Saída: True
print(usuario_salvo == "admin" and senha_salva == "errada") # Saída: False

# Exemplo Pratico: Validação de Meia-Entrada
idade = 18
possui_carteirinha = False

# Se for menor de 21 anos OU tiver carteirinha, tem direito
print(idade < 21 or possui_carteirinha == True) #Saída: True

#Exemplo Prático: Bloqueio de Sistema
sistema_manutencao = False

# Se o sistema NÃO está manutenção, permita o acesso
print(not sistema_manutencao == True) # Saída: True


