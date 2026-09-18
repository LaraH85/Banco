cadastro = {}

for i in range(2):
    print(f"Cadastro aluno {i+1}")
    nome = input("Insira os alunos: ")
    nota = float(input("Insira sua nota: "))

    cadastro[nome] = nota
    print(cadastro)

for nome, nota in cadastro.items():
    if nota >=7:
        print(nome,nota)
        print("Aprovado!")

