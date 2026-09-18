class ContaBancaria:
    def __init__(self, titular, saldo_inicial):
        self.__titular = titular        #atributo privado
        self.__saldo = saldo_inicial    #atributo privado

    def get_saldo(self):
        return self.__saldo

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            print(f"Depósito de R$ {valor: .2f} realizado!")
        else:
            print("Valor inválido para depósito!")

    def sacar(self, valor):
        if 0 < valor <= self.__saldo:
            self.__saldo -= valor
            print(f"Saque de R$ {valor: .2f} realizado!")
        else:
            print("Saque inválido! Saldo insuficiente ou valor inválido.")