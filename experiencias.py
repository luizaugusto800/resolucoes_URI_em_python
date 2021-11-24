num = int(input())

coelhos = 0
ratos = 0
sapos = 0
soma = 0
for i in range(num):
    entrada = input().split()
    soma += int(entrada[0])
    if entrada[1] == "C":
        coelhos += int(entrada[0])
    
    elif entrada[1] == "R":
        ratos += int(entrada[0])
    
    elif entrada[1] == "S":
        sapos += int(entrada[0])

print(f"""Total: {soma} cobaias
Total de coelhos: {coelhos}
Total de ratos: {ratos}
Total de sapos: {sapos}""")

p_c = (coelhos / soma) * 100
p_r = (ratos / soma) * 100
p_s = (sapos / soma) * 100

print(f"""Percentual de coelhos: {p_c:.2f} %
Percentual de ratos: {p_r:.2f} %
Percentual de sapos: {p_s:.2f} %""")