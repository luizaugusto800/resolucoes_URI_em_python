
while True:
    entrada = int(input())
    if entrada == 0: break

    resultado = []

    for i in range(entrada):
        lista = []
        for j in range(entrada):
            lista.append(1)
        resultado.append(lista)


    valor = 1
    cima = 0
    esq = 0
    baixo = entrada - 1
    direita = entrada - 1

    if entrada % 2 == 0:
        meio = entrada / 2
    else:
        meio = (entrada + 1) / 2

    
    while (valor <= meio):
        i = esq
        while (i <= direita):
            resultado[cima][i] = valor
            resultado[baixo][i] = valor
            i += 1

        i = cima + 1
        while (i < baixo):
            resultado[i][esq] = valor
            resultado[i][direita] = valor
            i += 1

        valor += 1
        cima += 1
        baixo -= 1
        esq += 1
        direita -= 1

    for i in range(entrada):
        acumulador = ""
        for j in range(entrada):
            acumulador += f"   {resultado[i][j]}"
        txt = ""
        for indice in range(1, len(acumulador)):
            txt += acumulador[indice]
        print(txt)

    print("")