#Radar de Velocidade Inteligente:
# Um radar emite multas severas se o motorista passar a mais de 20% acima do limite permitido da via (100 km/h).
# Escreva um script que diga se o motorista não foi multado,
# se recebeu multa média (até 120 km/h) ou multa grave (acima de 120 km/h).

velocidade = int(input("Digite uma velocidade em Km/h: "))

if velocidade > 120:
    print(f"Acedeu a velocidade {velocidade}, multa grave!")

elif velocidade == 120:
    print(f"Velocidade {velocidade}, multa média! ")

else:
    print(f"Tudo certo!")