def fatorial(numero):

    numero = int(input('numero :'))
    if numero < 0:
        print('numero negativo')
    resultado = 1
    for i in range(1,numero +1):
        resultado *= i
    return resultado

print(fatorial(5))

