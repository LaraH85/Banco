#Desenvolva um programa que peça uma sequência de notas de avaliações de um projeto técnico.
# Após inserir cada nota, pergunte se o avaliador quer inserir outra.
# Se ele disser que não, encerre e imprima a maior nota informada.

while True:
    print("Digite sua nota!")

    nota = float(input("Digite a nota: "))
    pergunta = input("Gostaria de inserir outra nota (S/N): ")

    if pergunta.upper() == "N":
        print(f"Obrigado por usar o programa! Nota: {nota}")
        break

