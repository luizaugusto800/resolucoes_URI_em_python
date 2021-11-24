pares = 0
impares = 0
positivos = 0
negativos = 0
for i in range(5):
    num = float(input())
    if num % 2 == 0:
        pares += 1
    elif num % 2 == 1:
        impares += 1
    
    if num > 0:
        positivos += 1
    elif num < 0:
        negativos += 1

print(f"""{pares} valor(es) par(es)
{impares} valor(es) impar(es)
{positivos} valor(es) positivo(s)
{negativos} valor(es) negativo(s)""")
