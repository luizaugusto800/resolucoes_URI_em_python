valor = int(input())
medias = []
for i in range(valor):
    entrada = input(). split()
    media = ((float(entrada[0]) * 2) + (float(entrada[1]) * 3) + (float(entrada[2]) * 5)) / 10
    medias.append(media)

for i in range(len(medias)):
    print(f"{medias[i]:.1f}")
