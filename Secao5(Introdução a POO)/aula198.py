# class - Classes são moldes para criar objetos
# As classes geram novos objetos (instâncias) que
# podem ter seus próprios atributos e métodos.
# Os objetos gerados pela classe podem usar seus dados
# internos para realizar várias ações.
# Pascal case CriarBaseDeDados
# Por convenção, usamos PascalCase para nomes de
# classes.

class Pessoa:
    def __init__(self):
        self.nome = ''
        self.idade = 10


p1 = Pessoa()
p1.anoNascimento = 2002


print(p1.idade)
print(p1.anoNascimento)
