# mine sistema bancario : numero da conta, nome, cpf, conta fisica ou juridica, idade.
# 5 clientes na conta, 3 funções na conta: saque, transferencia e deposito.
# Primeiro em programação estruturada.

bancos = []

contador = 0
numero = 123456

print('---- SISTEMA BANCÁRIO ----\n')

while True:
    print('\nEscolha 1, 2, 3 ou 4!\n')
    print('1. Cadastro!')
    print('2. Funções da conta!')
    print('3. Conta cadastradas!')
    print('4. Sair do sistema!')

    escolha = input('\nInserir: ')

    match escolha:
        # ---------- CADASTRO ------------
        case '1':

            if contador >= 5:
                print('Conta física(PF) ou jurídica (PJ)\n')

                pessoa = input('Inserir: ').upper()

            #------------ PESSOA FÍSICA ---------------

            if pessoa == 'PF':
                    cpf = input('Documento : ')
                    cliente = input('Nome do cliente: ')
                    idade = int(input('Idade: '))
                    saldo = float(input('Saldo: '))

                    while len(cpf) != 11 or not cpf.isdigit():
                        print('Não pode ter menos de 11 numeros.')
                        cpf = input('Documento : ')

                    while idade < 18:
                        print('Não pode ser menor de 18 anos.')
                        idade = int(input('Idade: '))


                    banco = {
                        'numero': numero,
                        'tipo': 'PF',
                        'documento': cpf,
                        'cliente': cliente,
                        'idade': idade,
                        'saldo': saldo
                    }

                    bancos.append(banco)
                    print(f'Informações de {cliente} cadastradas!')
                    print('Número da conta:', numero)

                    numero += 1
                    contador = contador + 1

            #------------ PESSOA JURÍDICA ---------------

            elif pessoa == 'PJ':
                    cnpj = input('CNPJ: ')
                    empresa = input('Nome da empresa: ')
                    saldo = float(input('Valor do saldo: '))

                    while len(cnpj) != 14 or not cnpj.isdigit():
                        print('Não pode ter menos de 14 numeros.')
                        documento = input('CNPJ : ')

                    banco = {
                        'numero': numero,
                        'tipo': 'PJ',
                        'documento': cnpj,
                        'cliente': empresa,
                        'idade': None,
                        'saldo': saldo
                    }

                    bancos.append(banco)
                    print(f'Informações de {empresa} cadastradas!')

                    contador = contador + 1

            else:
                print('Nunhuma opcão escolhida!')

        case '2':
            print('--- FUNÇÕES DA CONTA ---')

            funcoes = input('Saque(S), Transferencia(T) ou Deposito(D)?').upper()

            if funcoes in ["S", 'Saque']:
                saque = int(input('Saque: '))
                bancos['saldo'] -= saque
                print('Saque concluido com sucesso.')

            elif funcoes in ['T', 'Transferencia']:
                transferencia = int(input('Transferencia: '))
                total = numero
                print('Transferencia concluida com sucesso.')

            elif funcoes in ['D', 'Deposito']:
                deposito = int(input('Deposito: '))
                bancos[banco['saldo'] += deposito
                print('Deposito feito com sucesso.')

            else:
                print('Nunhum escolhido!')

        case '3':

            if len(bancos) > 0:
                print('\n--- CLIENTES CADASTRADOS --- \n')
                for n in bancos:
                    print(f'Documento: {n["cpf"]} | Cliente: {n["cliente"]} | Idade: {n["idade"]} ')
                    print(f'Quantidade de pessoas:{contador}')
                    print(f'Saldo: {n["saldo"]}')

            else:
                print('Erro no programa!')

        case '4':
            print('Clientes cadastrados no banco:',contador)
            print('Obrigada, por usar nosso banco!')
            break
