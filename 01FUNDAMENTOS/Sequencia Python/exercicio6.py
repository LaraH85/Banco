'''Leia o nome, número de horas trabalhadas e o número de dependentes de um funcionário.
Após a leitura, escreva qual o Nome, salário bruto, os valores descontados para cada tipo de imposto e finalmente qual o salário líquido do funcionário.
Considerando que:
a) A empresa paga $12 por hora e $40 por dependentes.
b) Sobre o salário são descontados 8,5% p/ o INSS e 5% p/ IR'''

trabalhadores = input("Digite o numero de trabalhadores: \n")
horas = float(input("Digite as horas trabalhadas: \n"))
dependentes = float(input("Digite o numero de dependentes: \n"))

bruto = horas * 12 + dependentes * 40

inss = bruto * 0.085
ir = bruto * 0.05
liquido = bruto - ir - inss

print(f"Nome: {trabalhadores} ")
print(f"salario_bruto: {bruto:.2f} ")
print(f"deconto_INSS: {inss: .2f} ")
print(f"desoconto_IR: {ir: .2f}  ")
print(f"deconto_LIQUIDO: {liquido: .2f} ")

