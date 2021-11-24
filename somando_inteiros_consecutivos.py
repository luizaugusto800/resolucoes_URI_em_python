entrada = input().split()
for i in range(len(entrada)):
    if int(entrada[i]) >= 0:
        a = int(entrada[i])
        break

for i in range(len(entrada) - 1, -1, -1):
    if int(entrada[i]) > 0:
        n = int(entrada[i])
        break

soma = 0
for i in range(0, n):
    soma += a + i
print(soma)