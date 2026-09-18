#Uma escola deseja realizar um levantamento sobre o desempenho de seus alunos.
#Desenvolva um programa que permita cadastrar vários alunos.
#O programa deverá continuar solicitando dados até que o usuário escolha encerrar o cadastro.
#Para cada aluno, informe:

#Nome do aluno;
#Idade;

#Nota final (0 a 10).
#Ao final, o programa deverá exibir:
#1.Quantidade total de alunos cadastrados;
#2.Média geral das notas;
#3.Maior nota informada;
#4.Menor nota informada;
#5.Quantidade de alunos aprovados (nota maior ou igual a 6);
#6.Quantidade de alunos reprovados;
#7.Percentual de aprovados;
#8.Percentual de reprovados.

contador = 0
cadastro = 0
aprovado = 0
reprovado = 0

maior_numero = 10
menor_numero = 1

while True:
    print("== CADASTRO ==")

    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))
    nota = float(input("Digite a nota do aluno: "))

    contador += 1
    cadastro += nota
    
    if nota >= maior_numero:
        maior_numero = nota

    if nota <= menor_numero:
        menor_numero = menor_numero

    if nota >= 6:
        aprovado += 1
    else:
        reprovado += 1


    continua = input("Deseja continuar? [S/N]").upper()

    if continua != "S":
        break

    media = cadastro / contador
    percentual_aprovado = (aprovado / contador) *100
    percentual_reprovado = (reprovado / contador) *100

print("\n===== ESTATÍSTICAS =====")
print(f"1. Total de alunos cadastrados: {contador}")
print(f"2. Média geral das notas: {media:.2f}")
print(f"3. Maior nota: {maior_numero}")
print(f"4. Menor nota: {menor_numero}")
print(f"5. Quantidade de aprovados: {aprovado}")
print(f"6. Quantidade de reprovados: {reprovado}")
print(f"7. Percentual de aprovados: {percentual_aprovado:.2f}%")
print(f"8. Percentual de reprovados: {percentual_reprovado:.2f}%")
