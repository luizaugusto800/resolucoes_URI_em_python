soma = 0
a = 1
b = 1
while True:
    if a == 39: break
    soma += a / b
    a += 2
    b *= 2
print(f"{soma:.2f}")
