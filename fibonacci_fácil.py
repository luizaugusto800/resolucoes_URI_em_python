valor = int(input())

lista = [0, 1]
for i in range(valor - 2):
    soma = 0
    soma += lista[-1] + lista[-2]
    lista.append(soma)

acumulador = ""
for i in range(len(lista)):
    if i == len(lista) - 1:
        acumulador += f"{lista[i]}"
    else:
        acumulador += f"{lista[i]} "

print(acumulador)