n1 = int(input())
n2 = int(input())

if n1 < n2:
    for elemento in range(n1 + 1, n2):
        if elemento % 5 == 2 or elemento % 5 == 3:
            print(elemento)
else:
    for elemento in range(n2 + 1, n1):
        if elemento % 5 == 2 or elemento % 5 == 3:
            print(elemento)   