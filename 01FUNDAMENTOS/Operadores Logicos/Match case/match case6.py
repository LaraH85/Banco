#Cálculo de IMC Real:
# Peça o peso e a altura do usuário,
# calcule o IMC e use elif para classificar:
# Abaixo de 18.5 "Abaixo do peso",
# até 24.9 "Peso ideal",
# 25 ou mais "Sobrepeso".

peso = int(input("Digite o Peso: "))
altura = float(input("Digite sua altura: "))

altura = altura * 1
peso = peso / (altura * altura)

if peso < 18.5:
    print("Abaixo do peso!")
elif peso <= 24.9:
    print("Peso ideal!")
elif peso <= 25:
    print("Sobrepeso!")
elif peso <= 30:
    print("Obesidade!")
else :
    print("Obesidade grave!")