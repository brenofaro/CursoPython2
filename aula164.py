def concatenar(string_inicial):
    valor_final = string_inicial

    def interna(valor_a_concatenar):
        nonlocal valor_final  # Argumento para informar que a variavel nao é local (e fazer com que o python procure-a)
        valor_final += valor_a_concatenar
        return valor_final

    return interna


c = concatenar("a")

print(c("b"))
print(c("c"))
print(c("d"))
