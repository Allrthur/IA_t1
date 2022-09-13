import re

def filtrar_linhas(l):
    return l.split("	")[0:2]

dataset = open("files/dataset.txt", "r", encoding="utf8")

lines = dataset.read().split("\n")

filtered_lines = list(map(filtrar_linhas, lines))

#TODO: Retirar a pontuação de cada par de palavras

print(filtered_lines[0:1000])






