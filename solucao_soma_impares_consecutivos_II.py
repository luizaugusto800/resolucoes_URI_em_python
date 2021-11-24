def maximo(lista):
    maior = lista[0]
    for i in range(len(lista)):
        if lista[i] > maior:
            maior = lista[i]
    return maior

def minimo(lista):
    menor = lista[0]
    for i in range(len(lista)):
        if lista[i] < menor:
            menor = lista[i]
    return menor

entrada = int(input())

for i in range(entrada):
    linha = [int(num) for num in input().split()]

    soma = 0
    for valor in range(minimo(linha) + 1, maximo(linha)):
        if valor % 2 == 1:
            soma += valor
    print(soma)