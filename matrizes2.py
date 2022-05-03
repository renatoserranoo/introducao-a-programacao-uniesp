import linecache

import random

matriz = []

for x in range(1, 11):

    lista_auxiliar = []

    for j in range(10):
        lista_auxiliar.append(random.randint(0, 100))

    matriz.append(lista_auxiliar)

for linha in matriz:
    print(linha)

resultado_soma = 0

for l in matriz:

    for c in l:

        resultado_soma += c

print(f'Resultado da Soma = {resultado_soma}')

matrizb = []

for l in range(0, len(matriz)):

    lista_auxiliar = []

    for c in range(0, len(matriz[l])):

        resultado_multiplicacao = matriz[l][c] * 3
        lista_auxiliar.append(resultado_multiplicacao)

    matrizb.append(lista_auxiliar)

print(matrizb)
