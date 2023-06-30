# Métodos de classe + factories (fábricas)
# São métodos onde "self" será "cls", ou seja,
# ao invés de receber a instância no primeiro
# parâmetro, receberemos a própria classe.

class Pessoa:
    ano = 2023

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod
    def metodo_de_classe(cls):  # Cls contem a classe (o molde) enquanto self é sobre a instância
        print("Metodo de classe")

    @classmethod
    def criar_com_50_anos(cls, nome):
        return cls(nome, 50)

    @classmethod
    def criar_sem_nome(cls, idade):
        return cls("Anonima", idade)


p1 = Pessoa("joao", 26)

p2 = Pessoa.criar_com_50_anos("Vitoria")
print("Pessoa 50 anos:")
print(p2.nome)
print(p2.idade)
p3 = Pessoa.criar_sem_nome(20)
print("Pessoa sem nome:")
print(p3.nome)
print(p3.idade)