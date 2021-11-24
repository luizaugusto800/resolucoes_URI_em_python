num = int(input())

for i in range(num):
    numero = int(input())
    if numero == 0:
        print("NULL")
    
    if numero % 2 == 0:
        if numero > 0:
            print("EVEN POSITIVE")

    if numero % 2 == 0:
        if numero < 0:
            print("EVEN NEGATIVE")

    if numero % 2 == 1:
        if numero > 0:
            print("ODD POSITIVE")

    if numero % 2 == 1:
        if numero < 0:
            print("ODD NEGATIVE")