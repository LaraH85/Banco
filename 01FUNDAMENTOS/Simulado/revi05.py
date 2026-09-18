#Questão 5 – Padronização de Cadastros (1,0 ponto)
#Uma biblioteca digital identificou que muitos usuários cadastravam títulos de livros utilizando diferentes padrões de escrita,
# dificultando as pesquisas realizadas no sistema.
#Para minimizar esse problema, foi solicitado o desenvolvimento de um programa capaz de fornecer algumas informações sobre cada título informado.
#O programa deverá:
from xml.dom.minidom import ProcessingInstruction

#solicitar o título de um livro;
#informar a quantidade de caracteres;
#apresentar o título em letras maiúsculas;
#apresentar o título em letras minúsculas.

#Após cada cadastro, o sistema deverá perguntar se o usuário deseja cadastrar outro livro,
# permanecendo em execução até que seja escolhida a opção de encerramento.

while True:
    titulo = input('Digite o titulo do livro: ')

    if titulo == '':
        print('Erro: O título não pode estar vazio!')
    else:
        quantidade =len(titulo)
        titulo_maiusculo = titulo.upper()
        titulo_miniuculo = titulo.lower()

        print("\n--- Informações do Título ---")
        print(f"Título original: {titulo}")
        print(f"Quantidade de caracteres: {quantidade}")
        print(f"Título maiuculo: {titulo_maiusculo}")
        print(f"Título miniuculo: {titulo_miniuculo}")

    opcao = input("Deseja continuar ? [S/N] ")

    if opcao == 'N' or opcao == 'n':
        print('Encerrando o sistema...')
        break