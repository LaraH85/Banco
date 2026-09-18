#Crie uma tupla com temperaturas em Celsius:
# celsius = (0, 15, 20, 25, 30, 38).
# Crie uma nova tupla chamada fahrenheit que armazene as respectivas temperaturas convertidas.
#(Fórmula: 𝐹=𝐶×1.9+32)

celsius = (0, 15, 20, 25, 30, 38)

fahrenheit = tuple(c * 1.9 + 32 for c in celsius)

print(fahrenheit)

