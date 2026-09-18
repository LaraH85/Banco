#Uma linha de crédito estudantil exige que o aluno tenha média escolar maior ou igual a 7.0
#e que a renda familiar seja menor que $R\$\,2500.00$.
#Monte o código de verificação.

media_escolar = float(input("Digite sua media_escolar: "))
renda_familiar = float(input("Digite sua renda_familiar: "))

if media_escolar >= 7.0:
    entrou = True

if renda_familiar < 2500.00:
    entrou = True

print(media_escolar >= 7.0 or renda_familiar < 2500.00)
print(f'renda_familiar: R${renda_familiar}')
