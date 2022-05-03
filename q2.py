import random
vet = []
for num in range(1, 51):
    vet.append(random.randint(1, 50))
print(f'O vetor criado foi: {vet}')

for i in range(0, len(vet)):
    print(f'Valor testado: {vet[i]}| Indice testado: {i}')
    for j in range(0, len(vet)):
        if vet[i] == vet[j] and i != j:
            print(f'Índice: {j} | Valor: {vet[j]} \n')
