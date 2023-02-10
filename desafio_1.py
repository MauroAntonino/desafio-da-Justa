"""
Escreva uma função, que receba um parâmetro de uma lista de String contendo dois elementos. 
Cada elemento contém uma string com sequência de números ordenados de forma crescente. 
E sua função deve retornar uma String contendo os números ordenados que aparecem nas duas listas:

Entrada: ["1, 3, 4, 7, 13", "1, 2, 4, 13, 15"]
Saída: 1,4,13

Entrada: ["1, 3, 9, 10, 17, 18", "1, 4, 9, 10"]
Saída: 1,9,10
"""
import json

entrada = input()

def solução(entrada):
    if type(entrada) != list:
        entrada = json.loads(entrada)
    
    #armazena as duas strings das listas
    string_1, string_2 = entrada[0], entrada[1]

    # fatia as strings em listas por meio das vírgulas
    # remove espaços vazios das strings na função trim_entry
    lista_1 = trim_entry(list(string_1.split(",")))
    lista_2 = trim_entry(list(string_2.split(",")))

    #indica o começo dos indices que serão iterados
    indice_1 = 0
    indice_2 = 0

    lista_final = []


    # o laço incrementa os indices até alcaçar o taanho total da lista
    while indice_1 < len(lista_1) and indice_2 < len(lista_2):
        # é realizada uma busca binária já que as listas estão ordenadas, o que tem um custo O(log(n))
        # na função é retornada um boleano indicando se foi encontrado o item na lista e o índice deste item
        # caso não seja encontrado o item, é retornado o indice do maior valor encontrado que seja menor que o item
        # este indice é utilizado para diminuir o tamanho da lista e consequente mente o tempo de execução da busca
        boleano, indice = binary_search(lista_2, lista_1[indice_1], low=indice_2)
        if boleano == True:
            # adiciona o valor na list afinal, de forma já ordenada
            lista_final.append(lista_2[indice])
            indice_1 += 1
            indice_2 = indice
        
        if boleano == False:
            indice_1 += 1  

    final = repr(lista_final)
    return "".join(final[1:len(final) - 1])

def trim_entry(arr):
    return [ int(item.strip()) for item in arr ]


def binary_search(arr, x, low):
    # low = 0
    high = len(arr) - 1
    mid = 0
 
    while low <= high:
 
        mid = (high + low) // 2
 
        if arr[mid] < x:
            low = mid + 1
 
        elif arr[mid] > x:
            high = mid - 1
 
        else:
            return True, mid
 
    return False, mid

print(solução(entrada))

