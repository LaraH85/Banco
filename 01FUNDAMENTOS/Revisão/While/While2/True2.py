#Escreva um programa que simule a digitação de um PIN de segurança bancária de 4 dígitos.
# O loop executa pedindo o PIN.
# Se o PIN digitado for correto ("2026"), o loop quebra.
# Caso contrário, informa o erro e pede novamente.

import time
while True:
    print("Digite seu PIN!")
    time.sleep(1)

    pin = int(input("Digite o numero: "))

    if pin == 2026:
        print("Pin correto!")
        break
    else:
        print("Pin incorreto!")


