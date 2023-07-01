# Relações entre classes: associação, agregação e composição
# Composição é uma especialização da agregação.
# Mas nela, quando o objeto "pai" for apagado, todas
# as referências dos objetos filhos também são
# apagadas.

class Cliente:
    def __init__(self, nome):
        self.nome = nome
        self.enderecos = []

    def inserir_endereco(self, rua, numero):
        self.enderecos.append(Endereco(rua, numero))

    def listar_enderecos(self):
        for endereco in self.enderecos:
            print(f"Rua = {endereco.rua} Numero = {endereco.numero}")

    def __del__(self):
        print("Apagando, ", self.nome)


class Endereco:
    def __init__(self, rua, numero):
        self.rua = rua
        self.numero = numero

    def __del__(self):
        print("Apagando, ", self.rua, self.numero)


c1 = Cliente("Maria")
c1.inserir_endereco("Av Brasil", 24)
c1.inserir_endereco("Rua A", 12)

c1.listar_enderecos()
print("#"* 30, "Aqui acaba o codigo")

del c1