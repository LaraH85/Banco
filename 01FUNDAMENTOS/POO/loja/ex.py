#produto =mostrar, comprar, utilizar/ para vendas, para pedidos
#cliente = procurar,comprar, utilizar / para comprar e visualizar
#funcionario = organizar, precificar, passar as compras / trabalhar, auxiliar
#fornecedor = levar, verificar, entregar / para trazer novos produtos e verificar para que não ocorra erros
#vendas = produto, valor, comprado / orfanizado, ser comprado

class Carro:
    pass

carro1 = Carro()
carro2 = Carro()
carro3 = Carro()

class Livro:
    pass

livro1 = Livro()
livro2 = Livro()

livro1.titulo = 'Multiversos'
livro1.autor = 'Antonio Lucas'
livro1.ano_publicacao = 1945
livro1.numero_paginas = 650

class Aluno:
    def __init__(self, nome,idade,curso):
        self.nome = nome
        self.idade = idade
        self.curso = curso

aluno1 = Aluno('Lucas', 15, 'Criação de Game')

print('Nome:',aluno1.nome)
print('Idade:',aluno1.idade)
print('Curso:',aluno1.curso)

