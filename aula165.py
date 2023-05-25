# Funções decoradoras

# Função Decoradora
def create_function(function):
    def interna(*args, **kwargs):
        # "Inicio da decoração"

        for arg in args:
            is_string(arg)
        resultado = function(*args, **kwargs)
        # "Fim da decoração"

        return resultado

    return interna


def inverte_string(string):
    def maiuscula_string():
        return

    return string[::-1]


def is_string(param):
    if not isinstance(param, str):
        raise TypeError("param deve ser uma string")


new_reverse = create_function(inverte_string)
invertida = new_reverse("123")

print(invertida)
