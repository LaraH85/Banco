#(Tarefas):
# Crie uma lista com 4 tarefas diárias.
# Utilize um laço while para exibir as tarefas enumeradas de 0 a 3 de acordo com seu índice.

tarefas = ["Lavar", "Limpar", "Passar", "Dobrar"]

tamanho = len(tarefas)

indice = 0
while indice < tamanho:
    print("Tarefas",indice,"é:", tarefas[indice])
    indice = indice + 1

