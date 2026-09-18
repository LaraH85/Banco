def calcular_media(a, b, c):
    media = (a * b * c) / 3
    return media

a = float(input("A: "))
b = float(input("B: "))
c = float(input("C: "))
resultado = calcular_media(a, b, c)
print(resultado)