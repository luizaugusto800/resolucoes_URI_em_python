n1 = int(input())
n2 = int(input())

soma = 0
if n1 < n2:
    for elemento in range(n1, n2 + 1):
        if elemento % 13 != 0:
            soma += elemento
else:
    for elemento in range(n2, n1 + 1):
        if elemento % 13 != 0:
            soma += elemento
print(soma)

