num = int(input())

lista = []
for i in range(6 * 2):
    lista.append(num + i)

for i in range(len(lista)):
    if lista[i] % 2 == 1:
        print(lista[i])