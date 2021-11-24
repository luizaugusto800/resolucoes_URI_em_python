operacao = input()

ordem = 12

matriz = []
for i in range(ordem):
    matriz.append([])

indice = 0
contador = 0
while True:
    elemento = input()
    matriz[indice].append(float(elemento))
    contador += 1

    if contador % ordem == 0:
        indice += 1

    if contador == ordem ** 2: break

soma = 0
contador = 0
for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        if i < j:
            soma += matriz[i][j]
            contador += 1
            if operacao == 'S':
                resultado = soma
            else:
                resultado = soma / contador

print(f'{resultado:.1f}')




