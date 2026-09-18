alunos = {}

for i in range(4):
    print(f"--- Cadastro de aluno {i} ---")
    nome = input("Nome: ")
    nota = float(input("Nota: "))
    alunos[nome] = nota

soma = 0
maior = 0
aluno_maior = ''

print('==== LISTA ====')
for nome, nota in alunos.items():
    print(f"Nome: {nome} | Nota: {nota:.1f}")
    soma += nota
    print(30*'=')

    if nota > maior:
        maior = nota
        aluno_maior = nome

media = soma / len(alunos)
print('\n======== ALUNO =========')
print(f'A nota do aluno: {media:.2f}')
print(f'O aluno com maior nota: {aluno_maior}, o aluno {alunos} ')
