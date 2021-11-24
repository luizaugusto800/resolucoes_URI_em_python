entrada = int(input())
for i in range(entrada):
    valores = input().split()
    if valores[1] == '0':
        print("divisao impossivel")
    else:
        print(f"{(int(valores[0]) / int(valores[1])):.1f}")
