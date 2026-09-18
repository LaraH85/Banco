#Peça a quantidade de alunos de uma turma e as notas de cada aluno. Ao final, calcule a média da turma.

quantidade_alunos = int(input("Quantidade de alunos: "))

for alunos in range(quantidade_alunos):
    pergunta = float(input("Digite a nota do aluno: "))

    media = quantidade_alunos / pergunta
print(f"A nota da turma deu {media}")
