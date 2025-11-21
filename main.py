tarefas = []

while True:
    print("\nMENU DE TAREFAS\n")
    print("1-Adicionar tarefas")
    print("2-Listar tarefas")
    print("3-Remover tarefas")
    print("4-Sair")

    opc = input("\nEscolha uma opção: ")

    if opc == "1":
        tarefa = input("\nDigite o nome da tarefa: ")
        tarefas.append(tarefa)

    elif opc == "2":
        print("\nTarefas atuais: ")
        if len(tarefas) == 0:
            print("\nNenhuma tarefa cadastrada.")
        else:
            for i, t in enumerate(tarefas):
                print(f"{i} - {t}")

    elif opc == "3":
        if len(tarefas) == 0:
            print("\nNão existem tarefas para remover.")
        else:
            indice = int(input("\nDigite o índice da tarefa que deseja remover: "))
            if 0 <= indice < len(tarefas):
                removida = tarefas.pop(indice)
                print(f"\nTarefa '{removida}' removida!")
            else:
                print("\nÍndice inválido!")

    elif opc == "4":
        print("\nFechando programa...")
        break

    else:
        print("\nNúmero invalido! Digite novamente.")