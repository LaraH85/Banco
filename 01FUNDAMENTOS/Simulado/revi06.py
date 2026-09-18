#Questão 6 – Sistema de Atendimento de uma Lanchonete (1,0 ponto)
#Uma lanchonete está substituindo sua calculadora por um pequeno sistema para realizar operações matemáticas durante o fechamento do caixa.
#Enquanto o operador estiver utilizando o sistema, deverá ser apresentado o seguinte menu:
#1 – Somar
#2 – Subtrair
#3 – Multiplicar
#4 – Dividir
#5 – Encerrar
#Sempre que uma operação for escolhida, o sistema deverá solicitar dois números, realizar o cálculo correspondente e apresentar o resultado.
#Caso o usuário informe uma opção inexistente, uma mensagem de erro deverá ser apresentada e o menu deverá ser exibido novamente.



print("--- Calculadora ---")
print("1 - Somar = '+'")
print("2 - Subtrair = '-'")
print("3 - Multiplicação = '*'")
print("4 - Divisao = '/'")
print("5 - Encerrar\n")

while True:

    operacao = input("Digite a operação que deseja realizar: ")

    if operacao == "1" :
        n1 = float(input('Digite um valor: '))
        n2 = float(input('Digite outro valor: '))
        resultado = n1 + n2
        print(f"O resultado deu {resultado}")

    elif operacao == '2' :
        n1 = float(input('Digite um valor: '))
        n2 = float(input('Digite outro valor: '))
        resultado = n1 - n2
        print(f"O resultado deu {resultado}")

    elif operacao == '3' :
        n1 = float(input('Digite um valor: '))
        n2 = float(input('Digite outro valor: '))
        resultado = n1 * n2
        print(f"O resultado deu {resultado}")

    elif operacao == '4' :
        n1 = float(input('Digite um valor: '))
        n2 = float(input('Digite outro valor: '))
        resultado = n1 / n2
        print(f"O resultado deu {resultado}")
    elif operacao == '5' :
        print("Encerrar o programa...")
        break

    else:
        print("Erro no programa...")
