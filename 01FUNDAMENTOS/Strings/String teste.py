divisor = "_" * 30
print(divisor)
print(" MENU PRINCIPAL DO SISTEMA ")
print(divisor)

nome = "Ana"
sobrenome = "Sobrenome"

nome_completo = nome + " " + sobrenome
print(nome_completo)

#ERRO CLASSICO DE JUNIOR
codigo_id = 404
#msg = "Erro detectado: " + codigo_id -> TypeError: can only concatenate str (not "int") to str

#Correção:
msg = "Erro detectado: " + str(codigo_id)

framework = "Django"
#Criamos uma nova string juntamos 'd' com o resto da string original do índice 1 em diante
framework = "d" + framework[1:]
print(framework) #Saída: django (Uma nova string ocupou o nome da variável)

entrada_usuario = "uSeR_nAmE@eMaIl.CoM"

email_limpo = entrada_usuario.lower()
print(email_limpo) # Saída: user_name@email.com

nome_sujo = "luiz carlos da silva"

print(nome_sujo.capitalize())
print(nome_sujo.title())

busca ="   notebook gamer   "

print(f"original: '{busca}'")
print(f"Limpo: '{busca.strip()}'") # Saída: 'notebook gamer'

preco_br = "R$ 1.450,90"
preco_EUA = preco_br.replace(".", ""). replace(",", ".")
print(preco_EUA)

log_erro = "ERROR: Falha na conexão. ERROR: Timeout de resposta."

print(log_erro.find("Falha")) # Saída: 7 (índice onde começa a palavra)
print(log_erro.count("ERROR")) # Saída: 2

arquivo = "relatorio_financeiro.csv"

if arquivo.endswith(".csv"):
    print("Iniciando a importação dos dados via planilha.")
else:
    print("Formato inválido. Envie um arquivo .csv")

frase = "Python para Desenvolvimento Web"
palavras = frase.split(" ")
print(palavras) # Saída: ['Python', 'para', 'Desenvolvimento', 'Web']

lista_tecnologias = ["Python", "Django", "FastAPI"]
resultado = " -> ".join(lista_tecnologias)
print(resultado) # Saída: Python -> Django -> FastAPI

token_seguranca = "A55B2"
print(token_seguranca.isdigit()) #False
print(token_seguranca.isalnum()) #True

comentario_suporte = "Prezados, o sistema está muito lendo hoje."

if "lento" in comentario_suporte:
    print("Prioridade: Alta. Direcionar ticket para equipe de infraestrutura.")

senha = "12345"

if len(senha_digitada) < 8:
    print("Senha fraca. A senha deve ter mínimo 8 caracteres.")

    print("Listagem de Erros:\n\t- Banco de dados offline\n\t- Falha de autenticação.")

texto_analise = "Engenharia de Software"
contador_vogais = 0
vogais = "aeiouAEIOU"

for caracter in texto_analise:
    if caracter in vogais:
        contador_vogais += 1

    print(f"O texto analisado possui {contador_vogais} vogais.")
