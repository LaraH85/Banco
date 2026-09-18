# Sistema bancário
# Número da conta, nome, CPF/CNPJ, conta física ou jurídica, idade.
# Máximo de 5 clientes
# 3 funções: saque, transferência e depósito
# Programação estruturada

bancos = []

contador = 0
numero = 123456

print('---- SISTEMA BANCÁRIO ----\n')

while True:

    print('\nEscolha 1, 2, 3 ou 4!\n')
    print('1. Cadastro!')
    print('2. Funções da conta!')
    print('3. Contas cadastradas!')
    print('4. Sair do sistema!')

    escolha = input('\nInserir: ')

    match escolha:

        case '1':

            # Limite de 5 clientes
            if contador >= 5:
                print('\nLimite de 5 clientes atingido!')
                continue

            print('\nConta física (PF) ou jurídica (PJ)?')

            pessoa = input('Inserir: ').upper()

            if pessoa == 'PF':

                cpf = input('Documento: ')

                while len(cpf) != 11 or not cpf.isdigit():
                    print('CPF deve possuir exatamente 11 números.')
                    cpf = input('Documento: ')

                cliente = input('Nome do cliente: ')

                idade = int(input('Idade: '))

                while idade < 18:
                    print('Não pode ser menor de 18 anos.')
                    idade = int(input('Idade: '))

                saldo = float(input('Saldo: '))

                banco = {
                    'numero': numero,
                    'tipo': 'PF',
                    'documento': cpf,
                    'cliente': cliente,
                    'idade': idade,
                    'saldo': saldo
                }

                bancos.append(banco)

                print(f'\nInformações de {cliente} cadastradas!')
                print('Número da conta:', numero)

                numero += 1
                contador += 1

            elif pessoa == 'PJ':

                cnpj = input('CNPJ: ')

                while len(cnpj) != 14 or not cnpj.isdigit():
                    print('CNPJ deve possuir exatamente 14 números.')
                    cnpj = input('CNPJ: ')

                empresa = input('Nome da empresa: ')

                saldo = float(input('Valor do saldo: '))

                banco = {
                    'numero': numero,
                    'tipo': 'PJ',
                    'documento': cnpj,
                    'cliente': empresa,
                    'idade': None,
                    'saldo': saldo
                }

                bancos.append(banco)

                print(f'\nInformações de {empresa} cadastradas!')
                print('Número da conta:', numero)

                numero += 1
                contador += 1


            else:
                print('Nenhuma opção escolhida!')

        case '2':

            if len(bancos) == 0:
                print('\nNenhuma conta cadastrada!')
                continue

            print('\n--- FUNÇÕES DA CONTA ---')

            numero_conta = int(input('Número da conta: '))

            # Procurar a conta
            conta = None

            for banco in bancos:

                if banco['numero'] == numero_conta:
                    conta = banco
                    break

            if conta is None:
                print('Conta não encontrada!')
                continue

            funcoes = input(
                'Saque (S), Transferência (T) ou Depósito (D)? '
            ).upper()

            if funcoes in ['S', 'SAQUE']:

                saque = float(input('Valor do saque: R$ '))

                if saque <= 0:
                    print('O valor deve ser maior que zero.')

                elif saque > conta['saldo']:
                    print('Saldo insuficiente!')

                else:
                    conta['saldo'] -= saque

                    print('Saque concluído com sucesso!')
                    print(f'Saldo atual: R$ {conta["saldo"]:.2f}')

            elif funcoes in ['T', 'TRANSFERENCIA']:

                numero_destino = int(
                    input('Número da conta de destino: ')
                )

                destino = None

                for banco in bancos:

                    if banco['numero'] == numero_destino:
                        destino = banco
                        break

                if destino is None:
                    print('Conta de destino não encontrada!')

                elif destino['numero'] == conta['numero']:
                    print('Não é possível transferir para a própria conta!')

                else:

                    transferencia = float(
                        input('Valor da transferência: R$ ')
                    )

                    if transferencia <= 0:
                        print('O valor deve ser maior que zero.')

                    elif transferencia > conta['saldo']:
                        print('Saldo insuficiente!')

                    else:

                        conta['saldo'] -= transferencia
                        destino['saldo'] += transferencia

                        print('Transferência concluída com sucesso!')
                        print(
                            f'Saldo atual: R$ {conta["saldo"]:.2f}'
                        )

            elif funcoes in ['D', 'DEPOSITO']:

                deposito = float(
                    input('Valor do depósito: R$ ')
                )

                if deposito <= 0:
                    print('O valor deve ser maior que zero.')

                else:

                    conta['saldo'] += deposito

                    print('Depósito feito com sucesso!')
                    print(
                        f'Saldo atual: R$ {conta["saldo"]:.2f}'
                    )

            else:
                print('Nenhuma função escolhida!')

        case '3':

            if len(bancos) > 0:

                print('\n--- CLIENTES CADASTRADOS ---\n')

                for n in bancos:

                    print(f'Número da conta: {n["numero"]}')
                    print(f'Tipo de conta: {n["tipo"]}')
                    print(f'Documento: {n["documento"]}')
                    print(f'Cliente: {n["cliente"]}')

                    if n['tipo'] == 'PF':
                        print(f'Idade: {n["idade"]}')

                    print(f'Saldo: R$ {n["saldo"]:.2f}')

                    print('-' * 40)


            else:
                print('Nenhuma conta cadastrada!')

        case '4':

            print('\nClientes cadastrados no banco:', contador)
            print('Obrigada por usar nosso banco!')

            break

        case _:

            print('Opção inválida!')