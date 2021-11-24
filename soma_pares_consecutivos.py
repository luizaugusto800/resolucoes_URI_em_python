soma = 0
while True:
    valor = int(input())
    if valor == 0: break
    
    contador = 0
    total = 0
    vezes = 0
    while True:
        if vezes == 5: break

        if contador % 2 == 0:
            valor += contador
            if valor % 2 == 0:
                total += valor
                contador = 0
                vezes += 1
            else:
                valor += 1
                total += valor
                contador = 0
                vezes += 1
        contador += 1

    print(total)
        

