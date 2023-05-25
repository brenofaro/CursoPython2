# Funções decoradoras

# Função Decoradora
def create_function(function):
    def intern(*args, **kwargs):
        # "Inicio da decoração"

        for arg in args:
            is_string(arg)
        resultado = function(*args, **kwargs)
        # "Fim da decoração"

        return resultado

    return intern


def reverse_string(string):
    return string[::-1]


def is_string(param):
    if not isinstance(param, str):
        raise TypeError("param deve ser uma string")


new_reverse = create_function(reverse_string)
reverse = new_reverse("123")

print(reverse)
