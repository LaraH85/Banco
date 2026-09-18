# Solicite um número inteiro positivo e calcule seu fatorial.

print("Digite numeros e saíra o fatorial do numero.")

pergunta = int(input('Digite o fatorial: '))
resultado = 1
contador = 1

while contador <= pergunta:
    resultado *= contador
    contador += 1

print(f"O resultado deu {resultado}")