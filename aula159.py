from pprint import pprint
from copy import deepcopy


def exibir(lista):
    pprint(lista)
    print()


produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]
produtos_novos = [
    {**p, 'preco': round(p['preco'] * 1.1, 2)}
    for p in deepcopy(produtos)
]
# for item in produtos_novos:                          # Outra forma de fazer
#     item['preco'] = round(item['preco'] * 1.1, 2)

exibir(produtos_novos)  # Produtos com 10 % a mais de preco

produtos_ordenados_por_nome_decre = sorted(
    deepcopy(produtos),
    key=lambda x: x['nome'].lower(), reverse=True
)

exibir(produtos_ordenados_por_nome_decre)

produtos_ordenados_por_preco_cresc = sorted(
    deepcopy(produtos),
    key=lambda x: x['preco']
)

exibir(produtos_ordenados_por_preco_cresc)