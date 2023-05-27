# map - para mapear dados | Pegar os dados, realizar modificacoes, e retornar outro dado
from pprint import pp
from functools import partial

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]


def aumentar_porcentagem(valor, porcentagem):
    return round(valor * porcentagem, 2)


# def criar_aumento_porcentagem(porcentagem):
#     def interna(valor):
#         return round(valor * (porcentagem / 100 + 1), 2)
#
#     return interna

# Map:
# É tipo uma list comprehension, pois aplica uma função para cada elemento de uma lista
aumentar_dez_porcento = partial(
    aumentar_porcentagem,
    porcentagem=1.1
)


# aumenta_dez_porcento = criar_aumento_porcentagem(10)

# novos_produtos = [
#     {**p, 'preco': aumentar_dez_porcento(p['preco'])} for p in produtos
#
# ]

def muda_preco_de_produtos(produto):
    return {
        **produto,
        'preco': aumentar_dez_porcento(
            produto['preco']
        )
    }


novos_produtos = map(
    muda_preco_de_produtos,
    produtos
)

pp(list(novos_produtos))
