l = int(input())
t = input()

tamanho = 12
soma = 0
for i in range(tamanho):
    for j in range(tamanho):
        valor = float(input())
        if i == l:
            soma += valor
            if t == "S":
                resultado = soma
            elif t == "M":
                resultado = soma / tamanho

print(f"{resultado:.1f}")

