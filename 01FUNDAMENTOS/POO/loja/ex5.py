class Produto:
    def __init__(self, nome, preco):
        self.__nome = nome
        self.__preco = preco

    def get__preco(self):
        return self.__preco

    def set_preco(self, preco):
        if preco > 0:
            self.__preco = preco
        else:
            print("Erro: O preço deve ser maior que 0")

cliente_produto = Produto('Notebook', 3000.00)
print(cliente_produto.get__preco())

print('\nValor negativo (-500)')
cliente_produto.set_preco(-500)

print('\nValor positivo (3000.00)')
cliente_produto.set_preco(3000)

print(f"Preço final: R$ {cliente_produto.get__preco():.2f}")

