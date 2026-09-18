#Questão 3 – Levantamento Demográfico (1,0 ponto)
#Uma prefeitura pretende ampliar os projetos esportivos oferecidos à população.
# Antes de definir quais atividades serão disponibilizadas, foi realizado um levantamento para conhecer o perfil etário dos participantes inscritos.
#O sistema deverá receber a idade de 25 participantes e, ao final da coleta, gerar um relatório contendo:

#quantidade de menores de idade;
#quantidade de maiores de idade;
#média das idades;
#maior idade informada;
#menor idade informada.

print("=== MAIOR E MENOR DE IDADE ===")

maior_idade = 0
menor_idade = 0
maior = None
menor = None

for idade in range(1, 6):
    pessoas = int(input("Digite sua idade: "))

    if pessoas >= 18:
        maior_idade += 1

    else:
        menor_idade += 1

    if maior is None or pessoas > maior:
        maior = pessoas
    if menor is None or pessoas < menor:
        menor = pessoas

media = maior_idade / maior_idade
print("\n=== RÉLATORIO ===")
print(f"Maiores de idade: {maior_idade}")
print(f"Menores de idade: {menor_idade}")
print(f"Média das idade informada: {media}")
print(f"Maior de idade citada: {maior}")
print(f"Maior de idade citada: {menor}")

