#Escreva um script que receba o código do estado civil de uma pessoa
# ('S' para Solteiro,
# 'C' para Casado,
# 'D' para Divorciado,
# 'V' para Viúvo)
# e imprima o texto descritivo correspondente por extenso.

estado_civil = input("Informe o estado civil: ")

match estado_civil:
    case "Solteiro":
        print("Solteiro")
    case "Casado":
        print("Casado")
    case "Divorciado":
        print("Divorciado")
    case "Viúvo":
        print("Viúvo")
    case _:
        print("Nenhum estado civil foi encontrado")