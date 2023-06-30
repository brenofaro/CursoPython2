# Relações entre classes: associação, agregação e composição
# Agregação é uma forma mais especializada de associação
# entre dois ou mais objetos. Cada objeto terá
# seu ciclo de vida independente.
# Geralmente é uma relação de um para muitos, onde um
# objeto tem um ou muitos objetos.
# Os objetos podem viver separadamente, mas pode
# se tratar de uma relação onde um objeto precisa de
# outro para fazer determinada tarefa.
# (existem controvérsias sobre as definições de agregação).
class Carrinho:
    def __init__(self):
        self._produtos = []

    @property
    def produtos(self):
        return self._produtos

    def total(self):
        return sum([p.preco for p in self._produtos])

    def listar_produtos(self):
        print("*" * 10)
        for produto in self._produtos:
            print(produto.nome, produto.preco)
        print("*" * 10)

    def inserir_produtos(self, *produtos):
        self._produtos.extend(produtos)

class Produto:
    def __init__(self, nome, preco):
        self._nome = nome
        self._preco = preco

    @property
    def nome(self):
        return self._nome

    @property
    def preco(self):
        return self._preco


carrinho = Carrinho()

p1, p2 = Produto('Caneta', 1.20), Produto("Caderno", 5)

carrinho.inserir_produtos(p1, p2)

carrinho.listar_produtos()
print(carrinho.total())