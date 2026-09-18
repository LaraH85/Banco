# Desenvolva um menu que permita ao usuário:
# Somar dois números;
# Subtrair dois números;
# Multiplicar dois números;
# Dividir dois números;
# Encerrar o programa.
# O menu deve continuar sendo exibido até o usuário escolher sair.
# Uma boa questão desafio para o final da lista deve exigir o uso conjunto de:

# Variáveis;

# Entrada e saída de dados;
# Operadores aritméticos;
# Operadores relacionais e lógicos;
# Estruturas condicionais;
# Estruturas de repetição;
# Contadores;
# Acumuladores;
# Sem utilizar listas, tuplas ou dicionários.

while True:
    print(f"Faça seu calculo, com (+), (-), (*), (/).")


    pergunta = input("Começar programa? [S/N]: ")

    if pergunta == "s":
        pergunta = pergunta.lower()

        operacao = input("Digite a operação que deseja realizar: ")

        if operacao == '+' :
            n1 = float(input('Digite um valor: '))
            n2 = float(input('Digite outro valor: '))
            resultado = n1 + n2
            print(f"O resultado deu {resultado}")

        elif operacao == '-' :
            n1 = float(input('Digite um valor: '))
            n2 = float(input('Digite outro valor: '))
            resultado = n1 - n2
            print(f"O resultado deu {resultado}")

        elif operacao == '*' :
            n1 = float(input('Digite um valor: '))
            n2 = float(input('Digite outro valor: '))
            resultado = n1 * n2
            print(f"O resultado deu {resultado}")

        elif operacao == '/' :
            n1 = float(input('Digite um valor: '))
            n2 = float(input('Digite outro valor: '))
            resultado = n1 / n2
            print(f"O resultado deu {resultado}")

        else:
            print("Erro no programa...")
    else:
        print("Encerrando o programa...")
        break