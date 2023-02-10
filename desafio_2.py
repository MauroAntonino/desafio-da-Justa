"""
Escreva uma função, que receba uma String e retorne a palavra mais longa desta String.

    Se houver duas ou mais palavras com o mesmo comprimento, retorne a primeira palavra mais longa da String.
    Ignore as pontuações e a situação em que a String será vazia.
    As palavras também podem conter números, mas somente as letras serão consideradas no tamanho da palavra.


Entrada: "Hello world123 567"
Saída: Hello

Entrada: "Justa é a fintech que mais cresce no Brasil"
Saída: fintech

Entrada: "Justino é o mascote da Justa"
Saída: Justino
"""
import json
import re
entrada = input()

def solução(string):
    string = json.loads(string)
    lista = re.split('\W+', string)
    maior_palavra = ""
    for item in lista:
        palavra = filtro_numeros(item)
        if len(palavra) > len(maior_palavra):
            maior_palavra = palavra

    return maior_palavra

def filtro_numeros(palavra):
    palavra = list(palavra)
    nova_palavra = []
    for item in palavra:
        if item.isalpha():
            nova_palavra.append(item)
    return "".join(nova_palavra)
        


print(solução(entrada))