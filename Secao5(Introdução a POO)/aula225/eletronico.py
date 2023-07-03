from log import LogFileMixin


class Eletronico:
    def __init__(self, nome):
        self._nome = nome
        self._ligado = False

    def ligar(self):
        if not self._ligado:
            self._ligado = True

    def desligar(self):
        if self._ligado:
            self._ligado = False


# # Não muito recomendado, pois esta deixando a classe mais complicada desnecessariamente
# class Smartphone(Eletronico, LogFileMixin):
#     def ligar(self):
#         super().ligar()
#
#         if self._ligado:
#             msg = f'{self._nome} está ligado'
#             self.log_success(msg)
#
#     def desligar(self):
#         super().desligar()
#
#         if not self._ligado:
#             msg = f'{self._nome} está desligado'
#             self.log_error(msg)

# Quase sempre melhor usar composicao do que herança
class Smartphone(Eletronico):
    def __init__(self, nome):
        super().__init__(nome)
        self.log_class = LogFileMixin()

    def ligar(self):
        super().ligar()

        if self._ligado:
            msg = f'{self._nome} está ligado'
            self.log_class.log_success(msg)

    def desligar(self):
        super().desligar()

        if not self._ligado:
            msg = f'{self._nome} está desligado'
            self.log_class.log_error(msg)

