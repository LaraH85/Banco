'''leia uma distância em km, o preço da gasolina em reais e exiba quantos litros de gasolina o carro irá consumir e
quanto será gasto em reais. Considere que o carro faz 12 km/l de gasolina.'''

distancia = float(input("Digite a distancia em KMs: "))
gasolina = float(input("Digite o preço da gasolina: "))

litros = distancia/ 12
gasto = litros * gasolina

print(f"litros consumidos: {litros:.2f} lt ")
print(f"gasto consumidos: {gasto:.2f} lt ")