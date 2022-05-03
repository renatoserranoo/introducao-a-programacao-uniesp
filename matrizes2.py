import linecache

import numpy
import random

matriz = []

for x in range(1, 11):
    lista_auxiliar = []
    for y in range(1, 11):
        lista_auxiliar.append(random.randint(1, 100))
    print('adicionando na matriz')
    print(lista_auxiliar)
    matriz.append(lista_auxiliar)

soma = numpy.sum(matriz)
print('soma da matriz')
print(soma)

matrizb = []

for l in range(0, len(matriz)):

    lista_auxiliar = []

    for c in range(0, len(matriz[l])):

        resultado_multiplicacao = matriz[l][c] * 3
        lista_auxiliar.append(resultado_multiplicacao)

    matrizb.append(lista_auxiliar)

print(matrizb)
