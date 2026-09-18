#Crie uma calculadora de operações básicas usando match case para ler os caracteres aritméticos (+, -, *, /)
# e executar a operação entre dois números.
numero1 = int(input("Informe um numero: "))
calculo = input("Informe os caracteres (+, -, *, /): ")
numero2 = int(input("Informe um numero: "))

match calculo:
    case "+":
        resultado = numero1 + numero2
        print(f"O resultado da adição é: {resultado} ")
    case "-":
        resultado = numero1 - numero2
        print(f"O resultado da soma é: {resultado} ")
    case "*":
        resultado = numero1 * numero2
        print(f"O resultado da mutiplicação é: {resultado} ")
    case "/":
        resultado = numero1 / numero2
        print(f"O resultado da divisão é: {resultado} ")
    case _:
        print("Calculo invalido!")