#Inicializamos a variável que controla o número de passos dados
passos_dados =0

#O loop continuará executanto enquanto o robô tiver dado menos de 3 passos
while passos_dados < 5:
    passos_dados = passos_dados + 1
    print(f"Robô deu o passo número {passos_dados}")

print("Objetivo alcançado! O robô parou.")

nemero_secreto = 7
total_tentativas = 0

while True:
    palpite = int(input("Adivinhe o número secreto (de 1 a 10): "))
    nemero_secreto += 1

    if palpite == nemero_secreto:
        print("Parabéns! Você acertou o número secreto.")
        break
    else:
        print("Palpite errado! Tente novamente.")

print(f"Você venceu o jogo após usar {total_tentativas} tentativa(s).")

# -----------------------------------------------------------------------

senha = "123senac"
tentativas = 5

senha = input("digite sua senha: ")

while senha != "123senac":
    print("senha incorreta tente novamente")
    print(f"{tentativas} tentativas")
    tentativas = tentativas - 1
    senha = input("digite sua senha: ")

    if tentativas == 0 or senha == "123senac":
        break
print(f"senha correta: {senha}")