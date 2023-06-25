import os

# Exercício lista de tarefas com opção de desfazer e refazer

lista_tarefas = []
lista_excluidos = []


def ler_lista(lista):
    if lista:
        for i, valor in enumerate(lista):
            print(f"Valor {i} = {valor}")
    else:
        print("A lista atual está vazia!")


def adicionar_tarefa(lista, tarefa):
    lista.append(tarefa)


def desfazer_acao(lista, lista_excluidos):
    if lista:
        lista_excluidos.append(lista.pop())
    else:
        print("Você não tem ações pra desfazer!")


def refazer_acao(lista, lista_excluidos):
    if lista_excluidos:
        lista.append(lista_excluidos.pop())
    else:
        print("Você não tem acoes para refazer!")


while True:
    ler_lista(lista_tarefas)
    print("Comandos: listar, desfazer, refazer")
    entrada = input("Digite uma tarefa ou comando: ")

    if entrada == 'desfazer':
        desfazer_acao(lista_tarefas, lista_excluidos)
        continue
    elif entrada == 'refazer':
        refazer_acao(lista_tarefas, lista_excluidos)
        continue
    elif entrada == 'listar':
        ler_lista(lista_tarefas)
        continue
    elif entrada == 'sair':
        print("Saindo do programa")
        break
    else:
        adicionar_tarefa(lista_tarefas, entrada)
        continue
