# Faça um programa que leia vários números.
# A entrada deve parar quando o usuário digitar 0.
# Ao final, informe a soma de todos os números digitados (exceto o zero).

print("Digite numero que deseja somar, caso não queira mais digite 0!")
numero = int(input("Digite um numero: "))

resultado = 0

for i in range(numero):
    pergunta = float(input(f"Digite um numero {i}: "))
    soma = pergunta + pergunta
    resultado += soma
    if pergunta == 0:
        break
print(f"O resultado deu {resultado}")