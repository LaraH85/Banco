biblioteca = {
    "nome": "",
    "idade": '',
    "curso" : "",
}

print('--- cadastro de aluno ---')

def cadastro(nome,idade,curso):
    biblioteca = {
        "nome": nome,
        "idade": idade,
        "curso": curso,
    }
    return biblioteca

nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))
curso = input('Digite sua curso: ')

dados = cadastro(nome,idade,curso)
print(dados)




