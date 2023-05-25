# Decoradores "Syntax Sugar"


# Funções decoradoras

# Função Decoradora
def create_function(function):
    def intern(*args, **kwargs):
        print("Vou te decorar")

        for arg in args:
            is_string(arg)
        result = function(*args, **kwargs)
        print("Você foi decorado")

        return result

    return intern  # Troca a função reverse_string por essa!


@create_function
def reverse_string(string):
    print(f"{reverse_string.__name__}")
    return string[::-1]


def is_string(param):
    if not isinstance(param, str):
        raise TypeError("param deve ser uma string")


reversed_variable = reverse_string("32134")

print(reversed_variable)
