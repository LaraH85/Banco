#Desenvolva um jogo onde o usuário deve adivinhar um número secreto (por exemplo, 7) quevocê definiu em uma variável.
# O programa deve continuar pedindo números até que ele acerte.
# Quando o usuário acertar, exiba: "Parabéns, você acertou!".

senha = ""

while senha != "1234":
    senha = input("Digite a senha secreta: ")
    if senha == "1234":
        print("Parabéns, você acertou!")

    else:
        print("tente novamente")