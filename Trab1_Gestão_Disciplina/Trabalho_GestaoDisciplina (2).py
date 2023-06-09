#Gustavo Gomes Contiero
#Declaração de Variáveis
num_alunos = int(input("Número de alunos: "))
num_trabalhos = int(input("Número de Trabalhos: "))
soma_media_sala = 0
aprovados = 0
reprovados = 0
recuperacao = 0

#Loop para coletar os dados de todos os alunos
i = 0
while i < num_alunos: 
    soma_trabalhos = 0

    #Coleta de dados
    print("=+=" * 15) 
    nome = input("Nome do(a) aluno(a): ")
    p1 = float(input("Nota da prova 1: "))
    p2 = float(input("Nota da prova 2: "))
    ps = float(input("Nota da prova substitutiva: "))

    #Verifica se a prova substitutiva teve nota maior que a p1 ou p2
    if ps > p1 or ps > p2:
        if ps > p1:
            p1 = ps
        else:
            p2 = ps
    soma_provas = p1 + p2

    #Loop que coleta as notas dos trabalhos    
    j = 0
    while j < num_trabalhos:
        trabalho = float(input(f"Nota trabalho {j + 1}: "))
        soma_trabalhos = soma_trabalhos + trabalho
        j += 1

    #Calculando as médias    
    media_provas = soma_provas/2
    media_trabalhos = soma_trabalhos/num_trabalhos
    media__final = (media_trabalhos*(0.4)) + (media_provas*(0.6))
    soma_media_sala += media__final
    print(f"Status de {nome}:")
    print(f"A média final : {media__final:.2f}")
    if media__final >= 6:
        print( "Aprovado(a)!! :)" )
        aprovados += 1
    elif media__final >= 4:
        print( "Recuperação." )
        recuperacao += 1
    else:
        print( "Reprovado(a). :(" )
        reprovados += 1
    i += 1

print("=+=" * 15) 
#Calculando a média da sala
media_sala = soma_media_sala/num_alunos
print(f"Alunos foram aprovados: {aprovados}")
print(f"Alunos estão de recuperação: {recuperacao}")
print(f"Alunos foram reprovados : {reprovados}")
print(f"A média final da sala foi: {media_sala:.2f}")