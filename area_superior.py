operacao = input()

ordem = 12

matriz = []
for i in range(ordem):
    matriz.append([])

for i in range(ordem):
    for j in range(ordem):
        elemento = float(input())  
        matriz[i].append(elemento)

soma = 0
contador = 0
for i in range(ordem):
    for j in range(i + 1, len(matriz[0]) - (i + 1)):
        soma += matriz[i][j]
        contador += 1   

        if operacao == 'S':
            resultado = soma
        else:
            resultado = soma / contador

print(f'{resultado:.1f}') 
