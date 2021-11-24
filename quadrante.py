while True:
    entrada = input().split()
    if int(entrada[0]) == 0 or int(entrada[1]) == 0: break

    if int(entrada[0]) > 0 and int(entrada[1]) > 0:
        print("primeiro")
    elif int(entrada[0]) < 0 and int(entrada[1]) < 0:
        print("terceiro")
    elif int(entrada[0]) > 0 and int(entrada[1]) < 0:
        print("quarto")
    else:
        print("segundo")