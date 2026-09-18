
print('======== CADASTRO DE ALUNOS ========')
cadastro = []

for i in range(5):
    nome = input('Nome do aluno: ')
    idade = int(input('Idade: '))
    nota = float(input('Nota: '))

    aluno = {
        'nome': nome,
        'idade': idade,
        'nota': nota
    }
    cadastro.append(aluno)

velho = cadastro[0]
novo = cadastro[0]
maior = cadastro[0]['nota']
menor = cadastro[0]['nota']
soma = 0
aprovados = 0
reprovados = 0

for aluno in cadastro:
    soma += aluno['nota']

    if aluno['idade'] > velho['idade']:
        velho = aluno
    if aluno['idade'] < novo['idade']:
        novo = aluno

    if aluno['nota'] > maior:
        maior = aluno['nota']
    if aluno['nota'] < menor:
        menor = aluno['nota']

    if aluno['nota'] >= 7.0:
        aprovados += 1
    else:
        reprovados += 1

media = soma / len(cadastro)

print('========= RELATÓRIO ===========')

print('\nTodos os alunos cadastrados: ')
for aluno in cadastro:
    print(f'Nome: {aluno["nome"]} | Idade: {aluno["idade"]} | Nota: {aluno["nota"]}')

print(f'\nAluno mais velho: {velho['nome']} ({velho['idade']} anos)')
print(f"Aluno mais novo: {novo['nome']} ({novo['idade']} anos)")
print(f'Maior nota: {maior}')
print(f'Menor nota: {menor}')
print(f'A média das notas: {media}')
print(f'Quantidade de alunos aprovados: {aprovados}')
print(f'Quantidade de alunos reprovados: {reprovados}')
