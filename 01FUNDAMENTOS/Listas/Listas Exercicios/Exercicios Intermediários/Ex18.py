#(Hotelaria): Um hotel armazena a idade de seus hóspedes atuais em uma lista.
# Escreva um programa que use um laço para exibir apenas as idades das pessoas que forem maiores de idade (18 anos ou mais).
print("=== HOTEL ===")
print("=== IDADE DE HÓSPEDES ===")

idades = [50,70,22,6,5,16,46,65,30,41,18]

for idade in idades:
    if idade >= 18:
        print('Idade dos hospedes:',idade)