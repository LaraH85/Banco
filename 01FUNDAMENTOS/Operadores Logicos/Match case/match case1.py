#Classificação de Triângulos:
# Receba três lados de um triângulo
# e verifique se ele é Equilátero (3 lados iguais),
# Isósceles (2 lados iguais) ou
# Escaleno (todos os lados diferentes).

lado1 = input("Verifique se o lado é Equilátero:")
lado2 = input("Verifique os lados do Isosceles:")
lado3 = input("Verifique do escaleto:")

if lado1 == lado2 == lado3:
    print("Equilátero")
elif lado1 == lado2 or lado2 == lado3:
    print("Isosceles")
else:
    print("Escaleno.")