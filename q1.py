import random
lista = []
for numeros in range(1, 21):
    lista.append(random.randint(0, 50))
lista.sort(reverse=True)
print(lista)
