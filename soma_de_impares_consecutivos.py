x = int(input())
y = int(input())

numeros = []
if x > y:
    for i in range(x - 1, y, -1):
        numeros.append(i)
elif x < y:
    for i in range(x + 1, y, 1):
        numeros.append(i)

soma = 0
for i in range(len(numeros)):
    if numeros[i] % 2 == 1:
        soma += numeros[i]

if x == y: soma = 0

print(soma)