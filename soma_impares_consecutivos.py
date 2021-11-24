def entrex_y(lista):
    soma = 0
    if lista[0] < lista[-1]:
        for elemento in range(int(lista[0]) + 1, int(lista[-1])):
            if elemento % 2 == 1:
                soma += elemento
    elif lista[0] > lista[-1]:
        for elemento in range(int(lista[1]) + 1, int(lista[0])):
            if elemento % 2 == 1:
                soma += elemento 
    return soma
 
entrada = int(input())
for i in range(entrada):
    numeros = input().split()
    print(entrex_y(numeros))