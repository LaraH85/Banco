funcionario = {
    "nome": "Fabricio",
    "salário": 2500,
    "cargo": "Assitente ADM"
}

funcionario["salário"] += 500

for chave, valor in funcionario.items():
    print(chave, ":", valor)