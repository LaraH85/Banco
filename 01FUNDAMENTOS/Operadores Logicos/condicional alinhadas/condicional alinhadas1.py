#Crie um sistema de processo seletivo.
# Primeiro, verifique se o candidato possui formação na área de TI.
# Se tiver, pergunte quantos anos de experiência ele possui.
# Se for maior que 2 anos, exiba "Candidato Avança para Entrevista", senão "Candidato para Banco de Talentos".
# Se não tiver formação, printe "Perfil incompatível".

processo_seletivo = input("Informe se possui formação na área de TI: ")

if processo_seletivo == "TI":
    print("seletivo")
    anos = int(input("Informe o numero de anos de experiência: "))

    if anos > 2:
        print("Candidato Avança para Entrevista")
    else:
        print("Candidato para Banco de Talentos.")
else:
    print("Perfil incompatível.")