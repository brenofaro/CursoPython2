# Criando Exceptions em Python Orientado a Objetos
# Para criar uma Exception em Python, você só
# precisa herdar de alguma exceção da linguagem.
# A recomendação da doc é herdar de Exception.
# https://docs.python.org/3/library/exceptions.html
# Criando exceções (comum colocar Error ao final)
# Levantando (raise) / Lançando (throw) exceções
# Relançando exceções
# Adicionando notas em exceções (3.11.0)

class MyError(Exception):
    ...


class Pessoa:
    def __init__(self, nome):
        self.nome = nome

    def falar(self):
        raise MyError(f"{self.nome} nao pode falar")


p1 = Pessoa("Carla")
p1.falar()
