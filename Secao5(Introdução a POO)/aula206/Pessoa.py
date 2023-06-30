# Exercício - Salve sua classe em JSON
# Salve os dados da sua classe em JSON
# e depois crie novamente as instâncias
# da classe com os dados salvos
# Faça em arquivos separados.
import json

CAMINHO_ARQUIVO = 'pessoa.json'


class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


p1 = Pessoa("Jao", 22)
p2 = Pessoa("Maria", 52)
p3 = Pessoa("Jose", 25)

lista = [vars(p1), vars(p2), vars(p3)]


def fazer_dump():
    with open(CAMINHO_ARQUIVO, "w") as file:
        json.dump(lista, file, indent=2)


if __name__ == 'main':
    fazer_dump()
