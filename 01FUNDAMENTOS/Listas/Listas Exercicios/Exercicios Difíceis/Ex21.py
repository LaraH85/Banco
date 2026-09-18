#21.(Segurança Computacional):
# Uma lista contém tentativas de logins maliciosos por minuto: [5, 12, 45, 8, 90, 2].
# Encontre o maior valor da lista utilizando apenas a estrutura for e um if interno (proibido usar a função max()).
print("=== SEGURANÇA COMPUTACIONAL ===")


listas = [5, 12, 45, 8, 90, 2]
numero_maior = listas[0]

for lista in listas:
    if lista > numero_maior:
        numero_maior = lista
print(numero_maior)