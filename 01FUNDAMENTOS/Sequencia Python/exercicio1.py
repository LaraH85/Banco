''' Leia um nome, idade e salário de um funcionário. Exiba os
mesmos dados lidos, no entanto o salário deve ser reajustado
em 12%. '''

name = input("Digite um nome: \n")
year = int(input("Digite a idade: \n"))
price = float(input("Digite o salário do funcionário: \n"))

porcent = (price*0.12)


print(name)
print(year)
print(price)
print(f'A salário é: R${+price+porcent} ')
