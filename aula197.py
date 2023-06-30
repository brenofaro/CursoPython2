# Positional-Only Parameters (/) e Keyword-Only Arguments (*)
# *args (ilimitado de argumentos posicionais)
# **kwargs (ilimitado de argumentos nomeados)
# 🟢 Positional-only Parameters (/) - Tudo antes da barra deve
# ser ❗️APENAS❗️ posicional.
# PEP 570 – Python Positional-Only Parameters
# https://peps.python.org/pep-0570/
# 🟢 Keyword-Only Arguments (*) - * sozinho ❗️NÃO SUGA❗️ valores.
# PEP 3102 – Keyword-Only Arguments
# https://peps.python.org/pep-3102/


# def soma(a, y, /, x, z): # Argumentos posicionais apenas, impede que o usuario especifique argumentos nomeados
#     print(a + y + x + z)
#

def soma(a,b, *, c): # Argumentos nomeados apenas, impede que o usuario especifique argumentos posicionais
    print(a+b)



soma(1,2,c=3)

