inter = 0
gremio = 0
contador = 0
empates = 0
while True:
    grenal = input().split()
    contador += 1
    if int(grenal[0]) > int(grenal[1]):
        inter += 1
    elif int(grenal[1]) > int(grenal[0]):
        gremio += 1
    elif inter == gremio:
        empates += 1

    pergunta = int(input("Novo grenal (1-sim 2-nao)"))
    if pergunta == 2: break

print(f"""{contador} grenais
Inter:{inter}
Gremio:{gremio}
Empates:{empates}""")

if inter > gremio:
    print("Inter venceu mais")
if gremio > inter:
    print("Gremio venceu mais")
if gremio == inter:
    print("Nao houve vencedor")