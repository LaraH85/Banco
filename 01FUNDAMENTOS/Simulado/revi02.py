#Questão 2 – Processo Seletivo de Bolsas (1,0 ponto)
#Uma instituição de ensino técnico concederá bolsas de estudos para estudantes com bom desempenho acadêmico.
# Para participar do processo seletivo, o candidato deverá atender simultaneamente aos seguintes critérios:

#Média final maior ou igual a 8,0;
#frequência mínima de 75%.
#O setor de Tecnologia da Informação foi responsável por desenvolver um programa para auxiliar a comissão avaliadora.

#Desenvolva um algoritmo que solicite:
#nome do candidato;
#média final;
#frequência (%).
#Ao final, informe se o candidato foi classificado ou não classificado, justificando o motivo da decisão.

print('=== PROCESSO SELETIVO ===\n')
print('-Média final maior ou igual a 8,0 para passar.')
print('-Frequência mínima de 75% nas aulas.\n')

contador = 0

while True:
    nome = input('Digite o nome do candidato:')
    media = float(input("Digite a média final do candidato:"))
    frequencia = float(input("Digite a frequência em (%):"))

    media_minima = 8.0
    frenquencia_minima = 75.0

    if media >= media_minima and frequencia >= frenquencia_minima:
        contador += 1
        print(f'\nO candidato {nome}: CLASSIFICADO ')
        print(f'Motivo: Atendeu os critérios da média final e frequência nas aulas.')

    else:
        print(f'\nO candidato {nome}: NÃO CLASSIFICADO ')
        print(f'Motivo: Média insuficiente, nota mínima: {media_minima:.1f}')
        print(f'Motivo: Frequência insuficiente, (%) mínima: {frenquencia_minima:.1f}%')

        if media < 0 or media >10:
            print('\nTente novamente... A média deve estar entre 0 e 10.')
        if frequencia < 0 or frequencia > 100:
            print('\nTente novamente... A frequência deve estar entre 0 e 100%.')

    pergunta = input('\nDigite se deseja continuar: (S/N)')

    if pergunta == 'N' or pergunta == 'n':
        print(f'\n-Estudantes cadastrados na bolsas: {contador}')
        break
