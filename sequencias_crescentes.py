num = int(input())
while True:
    acumulador = ""
    if num == 0: break
    for i in range(1, num + 1):
        if i != num:
            acumulador += f"{i} "
        elif i == num:
            acumulador += f"{i}"
    print(acumulador)
    num = int(input())
    
