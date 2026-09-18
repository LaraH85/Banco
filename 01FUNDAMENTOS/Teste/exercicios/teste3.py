def validar_cpf(cpf):
    # Remove pontos e hífen
    cpf = cpf.replace(".", "").replace("-", "")

    # Verifica se possui 11 dígitos
    if len(cpf) != 11:
        return False

    # Rejeita CPFs como 11111111111, 22222222222 etc.
    if cpf == cpf[0] * 11:
        return False

    # Calcula o primeiro dígito verificador
    soma = 0

    for i in range(9):
        soma += int(cpf[i]) * (10 - i)

    resto = soma % 11

    if resto < 2:
        primeiro_digito = 0
    else:
        primeiro_digito = 11 - resto

    # Confere o primeiro dígito
    if primeiro_digito != int(cpf[9]):
        return False

    # Calcula o segundo dígito verificador
    soma = 0

    for i in range(10):
        soma += int(cpf[i]) * (11 - i)

    resto = soma % 11

    if resto < 2:
        segundo_digito = 0
    else:
        segundo_digito = 11 - resto

    # Confere o segundo dígito
    if segundo_digito != int(cpf[10]):
        return False

    return True


# Testando a função
cpf = input("Digite seu CPF: ")

if validar_cpf(cpf):
    print("CPF válido!")
else:
    print("CPF inválido!")
