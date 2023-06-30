# Atributo de classe

class Pessoa:
    ano_atual = 2022
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade

p1 = Pessoa("Joao", 22)
p2 = Pessoa("Helena", 35)

print(p1.get_ano_nascimento())
print(p2.get_ano_nascimento())