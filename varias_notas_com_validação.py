soma = 0
contador = 0
media = 0
pergunta = 1
acao = True
while acao == True:
    nota = float(input())
    if nota < 0 or nota > 10:
        print("nota invalida")
    
    if 0 <= nota <= 10:
        soma += nota
        contador += 1
    
    if contador == 2:
        media = soma / 2
        print(f"media = {media:.2f}")
        contador = 0
        soma = 0
        while True:
            print("novo calculo (1-sim 2-nao)")
            pergunta = int(input())
        
            if pergunta == 1:
                acao = True
                break
            elif pergunta == 2:
                acao = False
                break

            