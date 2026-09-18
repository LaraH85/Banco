class Aluno:
    def __init__(self, nome, idade, nota1, nota2):
        self.nome = nome
        self.idade = idade
        self.nota1 = nota1
        self.nota2 = nota2

pessoa1 = Aluno("Felipe", 22, 8, 10)
pessoa2 = Aluno("Ana", 30, 6, 9)

print("aluno:",pessoa1.nome)
print("aluna:",pessoa2.nome)
