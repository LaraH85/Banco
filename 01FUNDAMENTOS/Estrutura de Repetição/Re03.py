#Faça um programa que leia e valide as seguintes informações:
#Nome: maior que 3 caracteres;
#Idade: entre 0 e 150;
#Salário: maior que zero;
#Estado Civil: 's', 'c', 'v', 'd';

nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))
salario = float(input('Digite sua salario: '))
estado_civil = input('Digite seu estado civil: ')

while len(nome) < 3:
    print("Caracter maior que 3 caracteres.")
    nome = input('Digite seu nome: ')

while idade < 0 or idade > 150:
    print("Digite sua idade entre 0 e 150.")
    idade = int(input('Digite sua idade: '))

while salario <= 0:
    print("Incorreto, salário maoir que zero.")
    salario = float(input('Digite sua salario: '))

match estado_civil:
    case "S":
        print("Solteiro/a")
    case "C":
        print("Casado/a")
    case "V":
        print("Viúvo/a")
    case "D":
        print("Divorciado/a")
    case _:
        print("Nenhum estado civil")


