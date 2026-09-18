'''Leia as variáveis inteiras n1 e n2 e troque o valor destas variáveis.
Isto é, n1 deve ficar com o valor de n2 e n2 deve ficar com o valor de n1.
Pense em utilizar uma terceira variável para auxiliar na troca dos valores.'''

n1 = int(input("Digite um valor: "))
n2 = int(input("Digite outro valor: "))
n3 = int(input("Digite mais um valor: "))

n1 = n2
n2 = n3
n3 = n1

print(f"Antes de n1 {n1}, n2 {n2} ")
print(f"Depois de n1 {n1}, n2 {n2} ")
