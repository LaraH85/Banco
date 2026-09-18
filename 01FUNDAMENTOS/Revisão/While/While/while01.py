#Crie um programa que faça uma contagem regressiva de 10 até 0 e termine exibindo a mensagem "Feliz Ano Novo!".

contador = 10

import time
print(f"Contagem regressiva!")

while contador > 0:
    print(f" {contador}")
    time.sleep(1)
    contador -= 1

print("Feliz ano novo!")
