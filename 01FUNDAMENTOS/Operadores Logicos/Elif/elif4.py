#Crie um classificador de velocidade de internet.
# O usuário informa a taxa de download (Mbps):
# Menor que 10 Mbps é "Básica",
# até 100 Mbps é "Moderna",
# acima disso é "Ultra Fibra".

classificador = float(input("Insira o classificador de velocidade: "))

if classificador < 10:
    print(f"Básica.")

elif classificador <= 100:
    print(f"Moderna.")

else:
    print(f"Ultra Fibra.")