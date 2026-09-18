estados = (
    'Maranhão','Piauí', 'Ceará','Pernambuco'
)

pergunta = input('Digite o nome do estado: ')

if pergunta in estados:
    local = estados.index(pergunta)
    print(f"O estado {pergunta} pertence a região do Nordeste.")
    print(f"Sua posição: {local}")
else:
    print(f"O estado {pergunta} não pertence a região do Nordeste.")