class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def mostrar(self):
        print(f'Nome: {self.nome} - R$ {self.preco:.2f}')

produto1 = Produto('Mouse Game', 59.90)
produto2 = Produto('Teclado Mecânico', 129.90)

produto1.mostrar()
produto2.mostrar()