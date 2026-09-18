#Você foi contratado para criar um jogo de contagem matemática automatizado. O programa deve
#contar de 1 até 30. Porém, toda vez que o número atual for múltiplo de 4 (ou seja, divisível por 4,
#como 4, 8, 12, 16...), o programa não deve mostrar o número, mas sim substituir a exibição pela
#palavra "PLIM!".

for i in range(0, 31):
    if i % 4 == 0:
        print("PLIM!")
    else:
        print(i)