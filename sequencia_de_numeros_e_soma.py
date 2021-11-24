while True:
    entrada = input().split()
    if int(entrada[0]) <= 0 or int(entrada[1]) <= 0: break
    
    soma = 0
    acumulador = ""
    if int(entrada[0]) < int(entrada[1]):
        for numero in range(int(entrada[0]), int(entrada[1]) + 1):
            acumulador += f"{numero} "
            soma += numero
    elif int(entrada[0]) > int(entrada[1]):
        for numero in range(int(entrada[1]), int(entrada[0]) + 1):
            acumulador += f"{numero} "
            soma += numero
    print(f"{acumulador}Sum={soma}")