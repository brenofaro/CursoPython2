# filter é um filtro funcional

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


aumentar_dez_porcento = partial(
    aumentar_porcentagem,
    porcentagem=1.1
)


def muda_preco_de_produtos(produto):
    return {
        **produto,
        'preco': aumentar_dez_porcento(
            produto['preco']
        )
    }


# novos_produtos = [
#     p for p in produtos
#     if p['preco'] > 10
# ]

novos_produtos = filter(
    lambda p: p['preco'] > 10,
    produtos
)

pp(produtos)
print()
pp(list(novos_produtos))
