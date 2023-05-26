# Exercício - Unir listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas
# listas na ordem.
# Use todos os valores da menor lista.
# Ex.:
# ['Salvador', 'Ubatuba', 'Belo Horizonte']
# ['BA', 'SP', 'MG', 'RJ']
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]
from itertools import zip_longest

lista_1 = ['Salvador', 'Ubatuba', 'Belo Horizonte', "Rio de Janeiro", "Sergipe"]
lista_2 = ['BA', 'SP', 'MG', 'RJ']


# lista_concatenada = [(x, y) for x, y in lista_1 for y in lista_2]

def zipper(lista1, lista2):
    lista_concatenada = []
    if len(lista1) < len(lista2):
        for i, cidade in enumerate(lista1):
            lista_concatenada.append((cidade, lista2[i]))
        return lista_concatenada
    else:
        for i, cidade in enumerate(lista2):
            lista_concatenada.append((lista1[i], cidade))
        return lista_concatenada


print(zipper(lista_1, lista_2))

print(list(zip_longest(lista_1,lista_2, fillvalue="Sem Estado")))
