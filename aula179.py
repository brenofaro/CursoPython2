# Funções recursivas e recursividade

def contagem_valores(inicial, final):
    if inicial >= final:
        return final

    return inicial + contagem_valores(inicial + 1, final)


print(contagem_valores(1, 10))


def fatorial(num):
    if num <= 1:
        return 1
    return num * fatorial(num - 1)


print(fatorial(10))
