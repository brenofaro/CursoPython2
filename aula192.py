import os

# Exercício lista de tarefas com opção de desfazer e refazer

lista_tarefas = []
lista_excluidos = []


def ler_lista(lista):
    if not lista:
        print("A lista atual está vazia!")
        return

    for i, valor in enumerate(lista):
        print(f"Valor {i} = {valor}")


def adicionar_tarefa(lista, tarefa):
    lista.append(tarefa)


def desfazer_acao(lista, lista_excluidos):
    if not lista:
        print("Você não tem ações pra desfazer!")
        return
    lista_excluidos.append(lista.pop())


def refazer_acao(lista, lista_excluidos):
    if not lista_excluidos:
        print("Você não tem acoes para refazer!")
        return
    lista.append(lista_excluidos.pop())


while True:
    ler_lista(lista_tarefas)
    print("Comandos: listar, desfazer, refazer")
    entrada = input("Digite uma tarefa ou comando: ")

    # Utilizando lambda para adiar a execução da função
    comandos = {
        'listar': lambda: ler_lista(lista_tarefas),
        'refazer': lambda: refazer_acao(lista_tarefas, lista_excluidos),
        'desfazer': lambda: desfazer_acao(lista_tarefas, lista_excluidos),
        'adicionar': lambda: adicionar_tarefa(lista_tarefas, entrada)
    }

    # Adiando a execucao da funcao
    comando = comandos.get(entrada) if comandos.get(entrada) is not None else comandos['adicionar']
    # Executando agora a funcao
    comando()

    # if entrada == 'desfazer':
    #     desfazer_acao(lista_tarefas, lista_excluidos)
    #     continue
    # elif entrada == 'refazer':
    #     refazer_acao(lista_tarefas, lista_excluidos)
    #     continue
    # elif entrada == 'listar':
    #     ler_lista(lista_tarefas)
    #     continue
    # elif entrada == 'sair':
    #     print("Saindo do programa")
    #     break
    # else:
    #     adicionar_tarefa(lista_tarefas, entrada)
    #     continue
