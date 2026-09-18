#Um sistema de logs de servidor registra linhas como: "2026-058-19 [ERROR] Falha de autentificação no banco".
#Escreva um extrator que capture apenas o nível do erro (o texto que estiver dentro dos colchetes, neste caso: ERROR).

log_erro = "2026-058-19 [ERROR] Falha de autentificação no banco"

print(log_erro.find("Falha"))
print(log_erro.count("ERROR"))