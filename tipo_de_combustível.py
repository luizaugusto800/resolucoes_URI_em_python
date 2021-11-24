alcool = 0
gasolina = 0
diesel = 0
while True:
    codigo = int(input())
    if codigo > 4 or codigo < 1:
        codigo = int(input())
    
    if codigo ==1:
        alcool += 1
    elif codigo == 2:
        gasolina += 1
    elif codigo == 3:
        diesel += 1
    elif codigo == 4:
        break

print(f"""MUITO OBRIGADO
Alcool: {alcool}
Gasolina: {gasolina}
Diesel: {diesel}""")