#Faça um programa que leia a quantidade de faltas de um aluno em um curso técnico.
#Se o número de faltas for maior que 15, exiba o aviso: "Atenção: Aluno em risco de reprovação por faltas!".

faltas = int(input("Quantidades de faltas: "))

if faltas > 15:
    print("Atenção: Aluno em risco de reprovação por faltas!")

else:
    print("Está aprovado!")
