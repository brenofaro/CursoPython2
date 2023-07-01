# Herança simples - Relações entre classes
# Associação - usa, Agregação - tem
# Composição - É dono de, Herança - É um
#
# Herança vs Composição
#
# Classe principal (Pessoa)
#   -> super class, base class, parent class
# Classes filhas (Cliente)
#   -> sub class, child class, derived class
# Evitar passar de 3 níveis de herança

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def falar_nome(self):
        print(self.__class__.__name__)



class Cliente(Pessoa):
    ...

class Aluno(Pessoa):
    ...

p1 = Pessoa("Pessoa", 19)
p1.falar_nome()
c1 = Cliente("Jose", 22)
c1.falar_nome()
a1 = Aluno("Carlos", 35)
a1.falar_nome()