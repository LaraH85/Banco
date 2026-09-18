#Questão 10 – Sistema de Avaliação Física (2,0 pontos)
#Uma rede de academias deseja desenvolver um sistema para auxiliar os professores na avaliação inicial de novos alunos.
#O programa deverá permitir o cadastro de vários alunos. Para cada aluno deverão ser informados:
#nome;
#idade;
#peso (kg);
#altura (m).
#O sistema deverá calcular o Índice de Massa Corporal (IMC), utilizando a fórmula:
#𝐼𝑀𝐶=pesoaltura2
#Em seguida, o aluno deverá ser classificado conforme a tabela:
# IMC
#Classificação
#Menor que 18,5
#Abaixo do peso
#Entre 18,5 e 24,9
#Peso normal
#Entre 25 e 29,9
#Sobrepeso
#Igual ou superior a 30
#Obesidade
#O programa deverá continuar cadastrando alunos até que o usuário escolha encerrar.
#Ao final, apresente:
#•quantidade total de alunos cadastrados;
#•média das idades;
#•maior IMC calculado;
#•menor IMC calculado;
#•quantidade de alunos classificados em cada faixa de IMC;
#•percentual de alunos com IMC considerado normal.

quantidade = 0
soma = 0
maior = 0
menor = 999

abaixo_peso = 0
peso_normal = 0
sobrepeso = 0
obesidade = 0

while True:
    print("\n--- Cadastro de Avaliação Física ---")
    print("'sair' para encerrar o programa.")

    nome = input("Digite o nome do aluno: ")

    if nome.lower() == "sair":
        break
    idade = int(input("Digite a idade: "))
    peso = float(input("Digite o peso: "))
    altura = float(input("Digite a altura: "))

    imc = peso / (altura ** 2)
    quantidade = quantidade + 1
    soma = soma + idade

    if imc > maior:
        maior = imc
    if imc < menor:
        menor = imc

        if imc < 18.5:
            clasificacao = "Abaixo do peso"
            abaixo_peso = abaixo_peso + 1
        elif imc < 25:
            clasificacao = "Peso normal"
        elif imc < 30:
            clasificacao = "Sobrepeso"
            sobrepeso = sobrepeso + 1
        else:
            clasificacao = "Obesidade"
            obesidade = obesidade + 1
        print(f"Resultado: IMC: {imc:.2f}, Classificação: {clasificacao}.")

        if quantidade > 0:
            media = soma / quantidade
            percentual = (peso_normal / quantidade) * 100

        print("=== RELATÓRIO DE AVALIAÇÃO ===")
        print(f"Total de alunos: {quantidade}")
        print(f"Média das idades: {media:.1f} anos")
        print(f"Maior IMC: {maior:.2f}")
        print(f"Menor IMC: {menor:.2f}\n")
        print(f"Abaixo do peso: {abaixo_peso}")
        print(f"Peso normal: {peso_normal:.2f}")
        print(f"Sobrepeso: {sobrepeso:.2f}")

        print(f"Obesidade: {obesidade:.2f}\n")
        print(f"Percentual de alunos: {percentual:.1f}%")
    else:
        print("Nenhum aluno foi encontrado.")