# groupby - Agrupando valores (itertools)

from pprint import pp
from itertools import groupby

alunos = [
    {'nome': 'Luiz', 'nota': 'A'},
    {'nome': 'Letícia', 'nota': 'B'},
    {'nome': 'Fabrício', 'nota': 'A'},
    {'nome': 'Rosemary', 'nota': 'C'},
    {'nome': 'Joana', 'nota': 'D'},
    {'nome': 'João', 'nota': 'A'},
    {'nome': 'Eduardo', 'nota': 'B'},
    {'nome': 'André', 'nota': 'A'},
    {'nome': 'Anderson', 'nota': 'C'},
]


def ordena(aluno):
    return aluno['nota']


alunos_ordenado = sorted(alunos, key=ordena)

grupos = groupby(alunos_ordenado, key=ordena)
for chave, grupo in grupos:
    print(chave)
    pp(list(grupo))
