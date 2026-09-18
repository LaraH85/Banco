#Crie um validador para saber se um ano digitado pelo usuário possui 365 ou 366 dias
# (Dica: cheque se ele é divisível por 4 para descobrir se é bissexto).

ano = int(input("Digite o ano:"))

divisao = ano/4
resto = ano%4

if resto == 0:
    bissexto = True
    print(f'o ano {ano} é bissexto tem 366 dias. ')

else:
    bissexto = False
    print(f'o ano {ano} é normal tem 365 dias. ')

