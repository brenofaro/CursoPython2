# class - Classes são moldes para criar objetos
# As classes geram novos objetos (instâncias) que
# podem ter seus próprios atributos e métodos.
# Os objetos gerados pela classe podem usar seus dados
# internos para realizar várias ações.
# Pascal case CriarBaseDeDados
# Por convenção, usamos PascalCase para nomes de
# classes.

class Pessoa:
    def __init__(self, nome, sobrenome, idade):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade


p1 = Pessoa("Jose", "dos Santos", 22)
p2 = Pessoa("Maria", "dos Anjos", 32)

print(p1.nome,p1.sobrenome)
print(p2.nome,p2.sobrenome)
