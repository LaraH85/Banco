#Um sistema de RH precisa receber o nome completo de um funcionario e
#exibir quantos letra ele possui no total (desconsiderando os espaços em branco)

nome = input('Digite o nome do Funcionario: ')

nome = nome.replace(" ", "")
print(nome)
print(len(nome))
