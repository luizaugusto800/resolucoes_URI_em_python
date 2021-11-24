n = int(input())

i = 1
while True:
    print(f"{i} {i ** 2} {i ** 3}")
    print(f"{i} {i ** 2 + 1} {i ** 3 + 1}")
    i += 1
    if i > n: break
