entrada = int(input())
for i in range(entrada):
    valores = input().split()
    pa = int(valores[0])
    pb = int(valores[1])
    g1 = float(valores[2]) / 100
    g2 = float(valores[3]) / 100
    anos = 0
    while True:
        pa += int(pa * g1)
        pb += int(pb * g2)
        anos += 1 
        
        if pa > pb or anos > 100: break
        
    if anos > 100:
        print(f"Mais de 1 seculo.")
    else:
        print(f"{anos} anos.")

    