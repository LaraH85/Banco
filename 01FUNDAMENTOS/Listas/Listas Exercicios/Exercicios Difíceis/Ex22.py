#22.(Recursos Humanos):
# Uma lista contém os salários de uma empresa.
# Calcule a média salarial.
# Em seguida, use outro laço para contar
# e exibir quantos funcionários ganham acima dessa média calculada.

print("=== RECURSOS HUMANOS ===")

salario_acima = 0
salario_abaixo = 0

salarios = [1500, 2500, 3500, 4500]
for salario in salarios:
    media = salario / len(salarios)
    if media > salario_acima:
        salario_acima =+ 1

    else:
        salario_abaixo =+ 1

print("A média salarial:", media)
print("Os salarios acima:", salario_acima)
print("Os salarios abaixos:", salario_abaixo)


