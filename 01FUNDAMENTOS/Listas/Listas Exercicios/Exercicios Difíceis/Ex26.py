#(Banco de Dados):
# Crie uma lista de códigos numéricos.
# Peça para o usuário digitar um código no teclado.

# O programa deve procurar na lista:

# se achar,mostra em qual índice ele está;
#  se não achar após varrer tudo, exiba "Código inexistente".

print('=== BANCO DE DADOS ===')
tentativas = 4

print('-Quantidade de tentativas 5\n')

numeros = [999, 561, 165, 105, 156, 914, 464]
codigo = float(input("Digite o código: "))

for numero in numeros:
    if codigo not in numeros:
        print("Código inexistente.")
        tentativas -= 1
        codigo = int(input("Digite o codigo: "))

        if tentativas == 0:
            print("Quantidade de tentativas esgotado.")
            break

    else:
        print("Código existente:", numeros.index(codigo))
        break









