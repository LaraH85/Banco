#Desenvolva um script para uma loja de veículos: pergunte se o cliente quer comprar um carro ou uma moto.
# Se for carro, pergunte se prefere Sedan ou Hatch.
# Se for moto, pergunte se prefere Street ou Trail.
# Exiba a resposta final do modelo escolhido.

loja = input("Informe quer comprar um carro ou moto: ")

if loja == "carro":
    print("Catégoria carro!")
    loja = input("Informe tipo de carro Sedan ou Hatch: ")
    if loja == "Sedan":
        print("Sedan!")
    else:
        print("Hatch!")

elif loja == "moto":
    print("Catégoria moto!")
    loja = input("Informe tipo de moto Street ou Trail: ")
    if loja == "Street":
        print("Street!")
    else:
        print("Trail!")

else:
    print("Nenhum carro ou moto foi encontrado!")
