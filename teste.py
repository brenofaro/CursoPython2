from pprint import pprint

lista = [
    {'nome': 'Luiz', 'sobrenome': 'miranda'},
    {'nome': 'Maria', 'sobrenome': 'Oliveira'},
    {'nome': 'Daniel', 'sobrenome': 'Silva'},
    {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
    {'nome': 'Aline', 'sobrenome': 'Souza'},
]


def retorna_nome(item):
    return item['sobrenome'].lower()


# lista.sort(key=retorna_nome)

lista.sort(key=lambda x: x['nome'])

pprint(lista)

string = 'oi'
