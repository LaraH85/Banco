#Peça para o usuário digitar um número inteiro.
# Em seguida, mostre a tabuada de multiplicação desse número (de 1 a 10).

contador = int(input("Digite o número:"))

for i in range(1,11):
    (resultado) = contador * i
    print(f"{contador} x {i} = {resultado}")
