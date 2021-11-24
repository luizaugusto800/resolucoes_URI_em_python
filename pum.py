n = int(input())
contador = 0
i= -1
while True:
    i += 2
    print(f"{i*2 - 1} {i*2} {i*2 + 1} PUM")
    contador += 1
    if contador == n: break