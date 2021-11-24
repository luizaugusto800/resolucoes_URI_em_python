soma = 0
contador = 0
while True:
    idade = int(input())
    if idade < 0: break
    soma += idade
    contador += 1
    
media = soma / contador
print(f"{media:.2f}")