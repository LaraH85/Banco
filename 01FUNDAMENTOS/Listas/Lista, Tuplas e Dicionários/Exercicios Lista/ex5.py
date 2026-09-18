tuplas = (
    'Azul',
    'Verde',
    'Amarelo',
    'Vermelho',
    'Preto'
)

pergunta = input('Digite uma cor: ')

if pergunta in tuplas:
    print(tuplas,'Existe!')
else:
    print(tuplas,"Não existe!")