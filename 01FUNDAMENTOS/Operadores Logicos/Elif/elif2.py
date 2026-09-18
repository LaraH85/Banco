#Crie um script que receba o peso de um lutador e indique sua categoria no campeonato:
# Até 65kg "Peso Pena", Até 80kg "Peso Médio", Acima disso "Peso Pesado".

peso = float(input("Peso em Kg: "))

if peso <= 65:
    print("Peso Pena")
elif peso <= 80:
    print("Peso Médio")
else:
    print("Peso Pesado")