#Desenvolver um programa em Python que permite ao usuário cadastrar,
#visualizar e remover tarefas por meio de um menu intertivo.

print("=== TAREFAS ===\n")
print("1 - Adicionar Tarefa")
print("2 - Lista de tarefas")
print("3 - Remover Tarefa")
print("4 - Sair\n")

listas = []

while True:
    adicionar = input("Escolha a opção: ")

    if adicionar == "1":
        tarefa = input("\nDigite a tarefa: ")
        listas.append(tarefa)
        print(f"Lista adicionada com sucesso!")

    elif adicionar == "2":
        len(listas)
        for i in range(len(listas)):
            print(f"{i} - {listas[i]}")

    elif adicionar == "3":
            remover = int(input("\nDigite a tarefa que gostaria de remover: "))
            listas.pop(remover)
            print(f"Lista removida com sucesso!")


    elif adicionar == "4":
        print("-"*30)
        print("Saindo do programa...")
        break

    else:
        print("Erro nas opções.")
