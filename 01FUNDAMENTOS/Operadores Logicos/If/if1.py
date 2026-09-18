#Escreva um programa que peça a temperatura atual em graus Celsius.
# Se a temperatura for maior que 35 graus, o sistema deve exibir o aviso: "Alerta de calor extremo!".

temperatura = float(input("Digite sua temperatura: "))

if temperatura > 35:
    print(f"Alerta de calor extremo! {temperatura}º Celsius")

else:
    print(f"Temperatura está normal! {temperatura}º Celsius")
