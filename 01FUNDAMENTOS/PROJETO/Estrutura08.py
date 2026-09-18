#Crie um simulador de votação simplificado.
# O programa deve perguntar repetidamente:
# "Deseja continuar votando? (S/N)".
# Enquanto o usuário responder "S", o programa continua.
# Se ele responder "N", o programa exibe "Votação encerrada!" e finaliza.

senha = ""

while senha != "N":
    senha = input("Deseja continuar votando? (S/N): ")
    if senha == "S":
        print("Continuar votação!")
    else:
        print("Votação encerrada!")
