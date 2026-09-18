tuplas = ('São Paulo','Rio de Janeiro','Brasília','Fortaleza','Salvador',
          'Belo Horizonte','Manaus','Curitiba','Recife','Goiânia','Belém',
          'Porto Alegre','Guarulhos','Campinas','São Luís','Maceió','Campo Grande',
          'São Gonçalo','Teresina','João Pessoa')

cidade = input('Digite o nome da cidade: ').strip()

estado_lower = [c.lower() for c in tuplas]

if cidade.lower() in estado_lower:
    print(f'Existe {cidade} a cidade!')

    posicao = estado_lower.index(cidade.lower())
    print(f"Posição na tupla: {posicao}")
else:
    print(f'Não existe {cidade} a cidade!')

print(f'Cidade cadastrada: {len(tuplas)}')