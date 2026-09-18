def calcular_media(nota1,nota2):
    media = (nota1 + nota2)/2
    return media

nota1 = float(input("Primeira nota: "))
nota2 = float(input("Segunda nota: "))
resultado = calcular_media(nota1, nota2)
print('Média =', resultado)

def area(base, altura):
    area = base * altura

base = float(input("Base: "))
altura = float(input("Altura: "))
print(area(base, altura))