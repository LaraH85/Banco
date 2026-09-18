#Crie uma tupla contendo os nomes de cinco cidades. Peça ao usuario um indice e exiba a cidade correspondente.

cidades = ("Uberaba", "Ituitaba","Uberlândia", "Araguari","Caldas Novas","Formiga")

informe = int(input("Informe uma cidade: "))

if informe == 0:
    print("Uberaba")
elif informe == 1:
    print("Ituitaba")
elif informe == 2:
    print("Uberlândia")
elif informe == 3:
    print("Araguari")
elif informe == 4:
    print("Caldas Novas")
elif informe == 5:
    print("Formiga")
else:
    print("Erro...")
