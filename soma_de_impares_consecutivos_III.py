entrada = int(input())
for i in range(entrada):
    num = input().split()
    soma = 0
    valor = int(num[0])
    if valor % 2 == 0:
        valor += 1
    cont = 1
    soma += valor
    while True:
        if cont == int(num[1]):break
        valor += 2
        soma += valor
        cont += 1
    print(soma)

