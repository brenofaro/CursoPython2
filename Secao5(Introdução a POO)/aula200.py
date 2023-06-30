# methods em instâncias

class Carro:
    def __init__(self, nome):
        self.nome = nome
        self.velocidade = 0

    def acelerar(self, valor):
        self.velocidade += valor

    def freiar(self, valor):
        if self.velocidade > 0:
            self.velocidade -= valor

    def __str__(self):
        return f"Velocidade atual do {self.nome} = {self.velocidade}"


c1 = Carro("Fusca")
c2 = Carro("Celta")
print(c1)
print(c2)

c1.acelerar(20)
c2.acelerar(50)


print(c1)
print(c2)

c1.freiar(20)
c1.freiar(20)


print(c1)