def dobro(numero):
    if numero % 2 == 0:
        return True
    else:
        return False

numero = int(input('numero :'))
if dobro(numero):
    print("Par!")
else:
    print("Impar!")