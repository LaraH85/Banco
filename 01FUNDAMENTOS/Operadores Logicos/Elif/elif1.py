#Escreva um programa que leia a nota de um aluno (0 a 10) e exiba seu conceito conceitual: A (nota >=9),
#B (nota >=7), C (nota >= 5) ou D (nota < 5).

nota = float(input("Digite a nota do aluno: "))

if nota >= 9:
    print("A")
elif nota >= 7:
    print("B")
elif nota >= 5:
    print("C")
else:
    print("D")