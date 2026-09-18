tecnologia = "PYTHON"

#Acessor com índice positivos
primeira_letra = tecnologia[0]  # 'P'
quarta_letra = tecnologia[3]  # 'H'

#Acessando com índices negativos
ultima_letra = tecnologia[-1] # 'N' (Último caractere)
penultima_letra = tecnologia[-2] # 'O' (Penúltimo caractere)

print(f"primeira letra: {primeira_letra}, Ultima letra: {ultima_letra}")


frase = "Desenvolvimento de Sistemas"

termo_1 = frase[0:15]
print(termo_1)

tudo_ate_pos_15 = frase[:15]
do_16_ate_o_fim = frase[16:]
print(do_16_ate_o_fim)

codigo = "P1Y2T3H405N"
apenas_letras = codigo[0:11:2]
print(apenas_letras)

codigo = "RECURSO"
palavra_invertida = codigo[::-1]
print(palavra_invertida)

