class Pessoa:

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


        ID = 22
        print(ID)

    def mostrar(self):
        print(f"Nome = {self.nome}\n"
              f"Idade = {self.idade}")


p1 = Pessoa("Jose", 32)
p2 = Pessoa("Carla", 25)

p1.mostrar()
p2.mostrar()
