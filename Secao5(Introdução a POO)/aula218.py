# Exercício com classes
# 1 - Crie uma classe Carro (Nome)
# 2 - Crie uma classe Motor (Nome)
# 3 - Crie uma classe Fabricante (Nome)
# 4 - Faça a ligação entre Carro tem um Motor
# Obs.: Um motor pode ser de vários carros
# 5 - Faça a ligação entre Carro e um Fabricante
# Obs.: Um fabricante pode fabricar vários carros
# Exiba o nome do carro, motor e fabricante na tela

class Carro:
    def __init__(self, nome):
        self.nome = nome
        self._motor = None
        self._fabricante = None

    @property
    def motor(self):
        return self._motor

    @motor.setter
    def motor(self, motor):
        self._motor = motor

    @property
    def fabricante(self):
        return self._fabricante

    @fabricante.setter
    def fabricante(self, fabricante):
        self._fabricante = fabricante

    def mostrar_dados(self):
        print(f"Nome: {self.nome}\n"
              f"Motor: {self.motor.nome}\n"
              f"Fabricante: {self.fabricante.nome}")


class Motor:
    def __init__(self, nome):
        self.nome = nome


class Fabricante:
    def __init__(self, nome):
        self.nome = nome


toyota = Fabricante("Toyota")
motor = Motor("2.0")
c1 = Carro("Corola")

c1.fabricante = toyota
c1.motor = motor
c1.mostrar_dados()

volks = Fabricante("Volkswagen")
motor2 = Motor("1.0")
c2 = Carro("Fusca")

c2.fabricante = volks
c2.motor = motor2
c2.mostrar_dados()
