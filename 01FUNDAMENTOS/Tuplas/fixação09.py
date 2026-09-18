#Crie um programa que armazene o nome de 3 alunos e suas respectivas notas em uma tupla de tuplas,
# no formato: ((Nome1, Nota1), (Nome2, Nota2), (Nome3, Nota3)).
# Varra essa estrutura e exiba o nome de cada aluno e se ele foi "Aprovado" (nota >= 7) ou "Reprovado" (nota < 7).

alunos = ("Lara", 9.5,"Aline", 6.0,"Lucas", 8.0)

nome1, notas1, nome2, notas2, nome3, notas3 = alunos

if notas1 >= 7:
    print("Aprovado!", nome1)
else:
    print("Reprovado!", nome1)
if notas2 >= 7:
    print("Aprovado!", nome2)
else:
    print("Reprovado!", nome2)
if notas3 >= 7:
    print("Aprovado!", nome3)
else:
    print("Reprovado!", nome3)
