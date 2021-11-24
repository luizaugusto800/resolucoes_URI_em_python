i = 0
j1 , j2, j3 = 1, 2, 3
j_1, j_2, j_3 = 0, 0, 0
v = 0
contador = 0
while True:
    j1 += j_1 / 10
    j2 += j_2 / 10
    j3 += j_3 / 10
    if v % 1 == 0:
        print(f"I={v:.0f} J={j1:.0f}")
        print(f"I={v:.0f} J={j2:.0f}")
        print(f"I={v:.0f} J={j3:.0f}")
    else:
        print(f"I={v:.1f} J={j1:.1f}")
        print(f"I={v:.1f} J={j2:.1f}")
        print(f"I={v:.1f} J={j3:.1f}")
    contador += 3
    i += 2
    j_1 += 2
    j_2 += 2
    j_3 += 2
    v = i / 10
    if contador == 18: break

