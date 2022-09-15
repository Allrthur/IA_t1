import re

def filtrar_linhas(l):
    return l.split("	")[0:2]

def retirar_pontuacao_string(s): #  retira o ponto de uma string singular usando regex
    return re.sub('[^A-Za-z0-9]+', ' ', s) # TODO: Ajustar o regex para incluir acentuações(?)

def retirar_pontuacao(f): # retira a pontuacao de uma lista de strings (par original, traducao)
    result = list(map(retirar_pontuacao_string, f))
    return result

dataset = open("files/dataset.txt", "r", encoding="utf8")

lines = dataset.read().split("\n")

filtered_lines = list(map(retirar_pontuacao, list(map(filtrar_linhas, lines))))

print(filtered_lines)






