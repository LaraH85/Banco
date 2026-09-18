aluno = {
    'nome': 'Ana',
    'nota1': 8,
    'nota2': 6
}

media = aluno['nota1'] + aluno['nota2']/2

for i in aluno:
    if media >=7:
        print(i,':' ,aluno[i])
        print(media)
        print('Aprovado!')
    else:
        print(i, ':',aluno[i])
        print(media)
        print('Reprovado!')