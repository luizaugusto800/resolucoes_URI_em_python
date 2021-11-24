x = int(input())
while True:
    z = int(input())
    if z > x: break

contador = 0
i = 0
soma = 0
while True:
    valor = x + i
    soma += valor
    i += 1
    contador += 1
    if soma > z: break

print(contador)