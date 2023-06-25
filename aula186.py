import os
# Criando arquivos com Python + Context Manager with
# Usamos a função open para abrir
# um arquivo em Python (ele pode ou não existir)
# Modos:
# r (leitura), w (escrita), x (para criação)
# a (escreve ao final), b (binário)
# t (modo texto), + (leitura e escrita)
# Context manager - with (abre e fecha)
# Métodos úteis
# write, read (escrever e ler)
# writelines (escrever várias linhas)
# seek (move o cursor)
# readline (ler linha)
# readlines (ler linhas)
# Vamos falar mais sobre o módulo os, mas:
# os.remove ou unlink - apaga o arquivo
# os.rename - troca o nome ou move o arquivo
# Vamos falar mais sobre o módulo json, mas:
# json.dump = Gera um arquivo json
# json.load


caminho = 'aula186.txt'

with open(caminho, 'a+', encoding='utf-8') as arquivo:
    arquivo.write("Testando escrever com acentos: não, é tudo mãe\n")

    arquivo.writelines(("Teste de linhas\n", "Linha 2\n"))

with open(caminho, 'r', encoding='utf-8') as arquivo:
    print(arquivo.read())
    arquivo.seek(0, 0)
    print(arquivo.readline().strip())
    print(arquivo.readline().strip())

# os.rename(caminho, "aula186-2.txt")
# os.remove(caminho)
