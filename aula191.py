# Problema dos parâmetros mutáveis em funções python
# Quando um parâmetro é mutável o python fica reutilizando-o

# Nao utilizar parâmetros mutáveis!!
# def adiciona_clientes(cliente, lista=[]):
#     lista.append(cliente)
#     return lista

def adiciona_clientes(cliente, lista=None):
    if lista is None:
        lista = []
    lista.append(cliente)
    return lista


clientes1 = adiciona_clientes("luiz")
adiciona_clientes("Joao", clientes1)


clientes2 = adiciona_clientes("Marcos")
adiciona_clientes("Josefina", clientes2)

print(clientes1)
print(clientes2)