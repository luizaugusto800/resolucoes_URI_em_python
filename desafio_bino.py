num = int(input())
numeros = input().split()

por_2 = 0
por_3 = 0
por_4 = 0
por_5 = 0
for i in range(len(numeros)):
  if int(numeros[i]) % 2 == 0:
    por_2 += 1

  if int(numeros[i]) % 3 == 0:
    por_3 += 1

  if int(numeros[i]) % 4 == 0:
    por_4 += 1

  if int(numeros[i]) % 5 == 0:
    por_5 += 1
        
print(f"""{por_2} Multiplo(s) de 2
{por_3} Multiplo(s) de 3
{por_4} Multiplo(s) de 4
{por_5} Multiplo(s) de 5""")