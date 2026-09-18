#Questão 4 – Controle de Qualidade Industrial (1,0 ponto)
#Uma indústria alimentícia realiza inspeções periódicas em sua linha de produção.
# Cada lote produzido recebe uma nota de qualidade variando de 0 a 10, atribuída pelo inspetor responsável.
# Como o número de lotes avaliados varia diariamente,
# decidiu-se que o sistema deverá continuar registrando notas até que o inspetor informe -1, indicando o encerramento da inspeção.

#Desenvolva um programa que apresente, ao final:
#Quantidade de lotes avaliados;
#média das notas;
#maior nota registrada;
#menor nota registrada.
#Caso nenhuma nota válida seja informada, o programa deverá exibir uma mensagem apropriada.

print('=== QUALIDADE INDUSTRIAL ===\n')

quantidade = 0
soma = 0
maior = -1
menor = 11

print('-Notas deveram ser de (0 a 10).')
print('Digite -1 para o encerramento da inspeção.\n')

while True:
    nota = float(input(f'Infome a nota do lote {quantidade + 1}:'))
    if nota == -1:
        break

    if nota < 0 or nota > 10:
        print('Nota inválida, leia novamente as informações. ')
    else:
        quantidade = quantidade + 1
        soma = soma + nota

        if nota > maior:
            maior = nota
        if menor < nota:
            menor = nota

if quantidade == 0:
    print("\nNenhuma nota válida informada.")
else:
    media = soma / quantidade
    print("\n=== RÉLATORIO FINAL DA INSPEÇÃO ===")
    print(f'Quantidade de lotes avalidados: {quantidade}')
    print(f'Média das notas : {media:.2f}')
    print(f'Maior nota registrada: {maior:.1f}')
    print(f'Menor nota registrada: {menor:.1f}')
    print("\nENCERRANDO PROGRAMA...")