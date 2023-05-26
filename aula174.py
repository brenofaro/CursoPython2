# Combinação permutacao e produto
# Combinação - A odem não importa
# Permutação/ Arrajo - A ordem importa
# Produto - A ordem importa e repete valores únicos
from itertools import combinations, permutations, product

from pprint import pp

pessoas = [
    'Jose', 'Maria', 'Carla', 'Vitoria'
]

camisetas = [
    ['preta', 'branca'],
    ['p', 'm','g'],
    ['masculino', 'feminino', 'unisex'],
    ['algodao', 'poliester']
]

#
# print("Combinações:\n")
# pp(list(combinations(pessoas, 2)))
# print("Permutações:\n")
# pp(list(permutations(pessoas, 2)))

pp(list(product(*camisetas)))