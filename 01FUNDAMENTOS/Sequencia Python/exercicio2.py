'''Leia a base e a altura de um triângulo. Em seguida, escreva a
área do mesmo usando a fórmula.'''

base = float(input("Digite o base: \n"))
altura = float(input("Digite altura: \n"))

area =(altura * base/2)

print(f"area = ({base} * {altura}) / 2 = {area:.2f}\n")
print(f"a area do triangulo é {area:.2f} m² \n")
