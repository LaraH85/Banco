#Crie um script que receba a nota de um estudante.
#Se for maior ou igual a 6.0, exiba "Aprovado", caso contrário exiba "Reprovado".

nota = float(input("Digite a nota do estudante: "))

if nota >= 6.0:
    print("Aprovado!")

else:
    print("Reprovado!")