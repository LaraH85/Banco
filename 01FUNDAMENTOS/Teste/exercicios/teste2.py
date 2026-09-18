from datetime import datetime


class Conta:
    """Classe base que representa uma conta bancária."""

    def __init__(self, numero, cliente, documento, saldo=0.0):
        self._numero = numero
        self._cliente = cliente
        self._documento = documento
        self._saldo = saldo
        self._extrato = []
        self._registrar_transacao('Abertura de conta', saldo)

    # ---- Propriedades (encapsulamento) ----
    @property
    def numero(self):
        return self._numero

    @property
    def cliente(self):
        return self._cliente

    @property
    def documento(self):
        return self._documento

    @property
    def saldo(self):
        return self._saldo

    @property
    def tipo(self):
        return 'Conta'

    # ---- Operações ----
    def _registrar_transacao(self, descricao, valor):
        agora = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
        self._extrato.append(f'{agora} - {descricao}: R$ {valor:.2f}')

    def depositar(self, valor):
        if valor <= 0:
            print('O valor deve ser maior que zero.')
            return False

        self._saldo += valor
        self._registrar_transacao('Depósito', valor)

        print('Depósito feito com sucesso!')
        print(f'Saldo atual: R$ {self._saldo:.2f}')
        return True

    def sacar(self, valor):
        if valor <= 0:
            print('O valor deve ser maior que zero.')
            return False

        if valor > self._saldo:
            print('Saldo insuficiente!')
            return False

        self._saldo -= valor
        self._registrar_transacao('Saque', -valor)

        print('Saque concluído com sucesso!')
        print(f'Saldo atual: R$ {self._saldo:.2f}')
        return True

    def transferir(self, destino, valor):
        if destino.numero == self._numero:
            print('Não é possível transferir para a própria conta!')
            return False

        if valor <= 0:
            print('O valor deve ser maior que zero.')
            return False

        if valor > self._saldo:
            print('Saldo insuficiente!')
            return False

        self._saldo -= valor
        destino._saldo += valor

        self._registrar_transacao(
            f'Transferência enviada (conta {destino.numero})', -valor
        )
        destino._registrar_transacao(
            f'Transferência recebida (conta {self._numero})', valor
        )

        print('Transferência concluída com sucesso!')
        print(f'Saldo atual: R$ {self._saldo:.2f}')
        return True

    def exibir_extrato(self):
        print(f'\n--- EXTRATO DA CONTA {self._numero} ---')

        if not self._extrato:
            print('Nenhuma movimentação registrada.')
        else:
            for linha in self._extrato:
                print(linha)

        print(f'Saldo atual: R$ {self._saldo:.2f}')

    def exibir_dados(self):
        print(f'Número da conta: {self._numero}')
        print(f'Tipo de conta: {self.tipo}')
        print(f'Documento: {self._documento}')
        print(f'Cliente: {self._cliente}')
        print(f'Saldo: R$ {self._saldo:.2f}')


class ContaPF(Conta):
    """Conta de Pessoa Física."""

    def __init__(self, numero, cliente, cpf, idade, saldo=0.0):
        super().__init__(numero, cliente, cpf, saldo)
        self._idade = idade

    @property
    def idade(self):
        return self._idade

    @property
    def tipo(self):
        return 'PF'

    def exibir_dados(self):
        super().exibir_dados()
        print(f'Idade: {self._idade}')


class ContaPJ(Conta):
    """Conta de Pessoa Jurídica."""

    def __init__(self, numero, cliente, cnpj, saldo=0.0):
        super().__init__(numero, cliente, cnpj, saldo)

    @property
    def tipo(self):
        return 'PJ'


class Banco:
    """Classe responsável por administrar as contas do banco."""

    LIMITE_CLIENTES = 5
    NUMERO_INICIAL = 123456

    def __init__(self):
        self._contas = []
        self._proximo_numero = Banco.NUMERO_INICIAL

    @property
    def total_contas(self):
        return len(self._contas)

    def limite_atingido(self):
        return self.total_contas >= Banco.LIMITE_CLIENTES

    @staticmethod
    def validar_cpf(cpf):
        return len(cpf) == 11 and cpf.isdigit()

    @staticmethod
    def validar_cnpj(cnpj):
        return len(cnpj) == 14 and cnpj.isdigit()

    def cadastrar_pf(self, cpf, cliente, idade, saldo):
        conta = ContaPF(self._proximo_numero, cliente, cpf, idade, saldo)
        self._contas.append(conta)
        self._proximo_numero += 1
        return conta

    def cadastrar_pj(self, cnpj, empresa, saldo):
        conta = ContaPJ(self._proximo_numero, empresa, cnpj, saldo)
        self._contas.append(conta)
        self._proximo_numero += 1
        return conta

    def buscar_conta(self, numero):
        for conta in self._contas:
            if conta.numero == numero:
                return conta
        return None

    def listar_contas(self):
        if not self._contas:
            print('Nenhuma conta cadastrada!')
            return

        print('\n--- CLIENTES CADASTRADOS ---\n')

        for conta in self._contas:
            conta.exibir_dados()
            print('-' * 40)


class SistemaBancario:
    """Classe responsável pela interface com o usuário (menu)."""

    def __init__(self):
        self.banco = Banco()

    def executar(self):
        print('---- SISTEMA BANCÁRIO ----\n')

        while True:
            print('\nEscolha uma opção!\n')
            print('1. Cadastro!')
            print('2. Funções da conta!')
            print('3. Contas cadastradas!')
            print('4. Extrato!')
            print('5. Sair do sistema!')

            escolha = input('\nInserir: ')

            match escolha:
                case '1':
                    self._cadastrar()
                case '2':
                    self._funcoes_conta()
                case '3':
                    self.banco.listar_contas()
                case '4':
                    self._extrato()
                case '5':
                    print(
                        '\nClientes cadastrados no banco:',
                        self.banco.total_contas,
                    )
                    print('Obrigada por usar nosso banco!')
                    break
                case _:
                    print('Opção inválida!')

    def _cadastrar(self):
        if self.banco.limite_atingido():
            print('\nLimite de 5 clientes atingido!')
            return

        print('\nConta física (PF) ou jurídica (PJ)?')
        pessoa = input('Inserir: ').upper()

        if pessoa == 'PF':
            self._cadastrar_pf()
        elif pessoa == 'PJ':
            self._cadastrar_pj()
        else:
            print('Nenhuma opção escolhida!')

    def _cadastrar_pf(self):
        cpf = input('Documento: ')

        while not Banco.validar_cpf(cpf):
            print('CPF deve possuir exatamente 11 números.')
            cpf = input('Documento: ')

        cliente = input('Nome do cliente: ')

        idade = self._ler_inteiro('Idade: ')
        while idade < 18:
            print('Não pode ser menor de 18 anos.')
            idade = self._ler_inteiro('Idade: ')

        saldo = self._ler_float('Saldo: ')

        conta = self.banco.cadastrar_pf(cpf, cliente, idade, saldo)

        print(f'\nInformações de {cliente} cadastradas!')
        print('Número da conta:', conta.numero)

    def _cadastrar_pj(self):
        cnpj = input('CNPJ: ')

        while not Banco.validar_cnpj(cnpj):
            print('CNPJ deve possuir exatamente 14 números.')
            cnpj = input('CNPJ: ')

        empresa = input('Nome da empresa: ')
        saldo = self._ler_float('Valor do saldo: ')

        conta = self.banco.cadastrar_pj(cnpj, empresa, saldo)

        print(f'\nInformações de {empresa} cadastradas!')
        print('Número da conta:', conta.numero)

    def _funcoes_conta(self):
        if self.banco.total_contas == 0:
            print('\nNenhuma conta cadastrada!')
            return

        print('\n--- FUNÇÕES DA CONTA ---')

        numero_conta = self._ler_inteiro('Número da conta: ')
        conta = self.banco.buscar_conta(numero_conta)

        if conta is None:
            print('Conta não encontrada!')
            return

        funcoes = input(
            'Saque (S), Transferência (T) ou Depósito (D)? '
        ).upper()

        if funcoes in ['S', 'SAQUE']:
            valor = self._ler_float('Valor do saque: R$ ')
            conta.sacar(valor)

        elif funcoes in ['T', 'TRANSFERENCIA']:
            numero_destino = self._ler_inteiro('Número da conta de destino: ')
            destino = self.banco.buscar_conta(numero_destino)

            if destino is None:
                print('Conta de destino não encontrada!')
            else:
                valor = self._ler_float('Valor da transferência: R$ ')
                conta.transferir(destino, valor)

        elif funcoes in ['D', 'DEPOSITO']:
            valor = self._ler_float('Valor do depósito: R$ ')
            conta.depositar(valor)

        else:
            print('Nenhuma função escolhida!')

    def _extrato(self):
        if self.banco.total_contas == 0:
            print('\nNenhuma conta cadastrada!')
            return

        numero_conta = self._ler_inteiro('Número da conta: ')
        conta = self.banco.buscar_conta(numero_conta)

        if conta is None:
            print('Conta não encontrada!')
            return

        conta.exibir_extrato()

    @staticmethod
    def _ler_inteiro(mensagem):
        while True:
            try:
                return int(input(mensagem))
            except ValueError:
                print('Digite um número válido.')

    @staticmethod
    def _ler_float(mensagem):
        while True:
            try:
                return float(input(mensagem))
            except ValueError:
                print('Digite um valor válido.')


if __name__ == '__main__':
    sistema = SistemaBancario()
    sistema.executar()