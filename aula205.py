# Atributo de classe

class Pessoa:
    ano_atual = 2022

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade


dados = {'nome': 'Joao', 'idade': 22}
p1 = Pessoa(**dados)
# print(p1.__dict__)
# p1.__dict__['nome'] = 'Eita'
print(vars(p1))
