#Declarando Variáveis
pinos_derrubados = input("Digite o número de pinos derrubados em cada jogadas: ").split()
for i in range(len(pinos_derrubados)):
    pinos_derrubados[i] = int(pinos_derrubados[i])
placar = []
frame = []
pontos = 0
ultimo_frame = len(placar) - 1

#Criando a Matriz(Placar)
num_frames = 0
i = 0
while num_frames < 10:
    if num_frames == 9:
        while i < (len(pinos_derrubados)):
            frame.append(pinos_derrubados[i])
            pontos += pinos_derrubados[i]
            i += 1
        placar.append(frame)
        num_frames = 10
    elif pinos_derrubados[i] == 10 and len(frame) == 0:
        frame.append(10)
        placar.append(frame)
        pontos += 10
        num_frames += 1
        frame = []
    else:
        frame.append(pinos_derrubados[i])
        pontos += pinos_derrubados[i]
    if len(frame) == 2:
        placar.append(frame)
        num_frames += 1
        frame = []           
    i += 1

#calculando pontos bonus
i = 0
num_jogadas = 0
while i < len(placar) - 1:
    
    #STRIKE
    if len(placar[i]) == 1:
        pontos += pinos_derrubados[num_jogadas + 1] + pinos_derrubados[num_jogadas + 2]
        num_jogadas += 1

    #SPEAR    
    elif placar[i][0] + placar[i][1] == 10:
        pontos += pinos_derrubados[num_jogadas + 2]
        num_jogadas += 2

    else:
        num_jogadas += 2    
    i += 1

#Mudando os simbolos nos frames 1 a 9
for i in range(len(placar) - 1):
    if len(placar[i]) == 1:
        placar[i][0] = "X"
        placar[i].append("_")
    elif placar[i][0] + placar[i][1] == 10:
        placar[i][1] = "/"

#Mudando os simbolos no frame 10
if len(placar[ultimo_frame]) == 3:
    for i in range(3):
        if placar[ultimo_frame][i] == 10:
            placar[ultimo_frame][i] = "X"   
        elif i < 2 and placar[ultimo_frame][1] != "/":    
            if placar[ultimo_frame][i] + placar[ultimo_frame][i + 1] == 10:
                    placar[ultimo_frame][i + 1] = "/"

#Imprimindo Valores      
for i in range(len(placar)):
    for j in range(len(placar[i])):
        print(placar[i][j] , end=" ")
    print(end="| ")

print()
print(f"Pontuação: {pontos}")