# super() e a sobreposição de membros - Python Orientado a Objetos
# Classe principal (Pessoa)
#   -> super class, base class, parent class
# Classes filhas (Cliente)
#   -> sub class, child class, derived class


# class MinhaString(str):
#     def upper(self):
#         print('CHAMOU UPPER')
#         retorno = super(MinhaString, self).upper()
#         print('DEPOIS DO UPPER')
#         return retorno

# class MinhaString(str):
#     def upper(self):
#         print("Chamou upper")
#         return super().upper()
#
#
# string = MinhaString("Luiz")
#
# print(string.upper())


class Pessoa:
    def falar(self):
        print("Oi")


class Cliente(Pessoa):
    def falar(self):
        print("Eu sou o cliente falando")


c1 = Cliente()
c1.falar()
print(Cliente.mro())