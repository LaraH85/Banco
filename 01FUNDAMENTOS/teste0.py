#Crie uma função que dado 2 numeros, retorne se a pesssoa passou, caso a meia for acima de 13.

def media(nota1, nota2):
    media = (nota1 + nota2) / 2
    if media > 13:
        print("Aprovado!")
    else:
        print("Reprovado!")

media(50, 15)



