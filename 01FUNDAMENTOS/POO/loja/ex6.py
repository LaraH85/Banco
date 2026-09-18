class ContaBancaria:
    def __init__(self):
        self.__titular = 'Conta Bancaria'
        self.__saldo = 5000.00

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        self.__saldo -= valor

    def mostrar_saldo(self):
        print(self.__saldo)
