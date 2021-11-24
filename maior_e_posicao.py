numeros = []
for i in range(100):
    inteiros = int(input())
    numeros.append(inteiros)

maior = numeros[0]
for i in range(len(numeros)):
    if numeros[i] > maior:
        maior = numeros[i]
        posicao  = i

print(maior)
print(posicao + 1)