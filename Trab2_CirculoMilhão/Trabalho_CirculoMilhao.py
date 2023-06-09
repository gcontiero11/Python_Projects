#Gustavo Gomes Contiero
#Declaração de Variáveis
n = int(input("Informe o número de pessoas no círculo: "))
x = int(input("Informe um número menor que o  número de pessoas no círculo: "))

print("=+=" * 15)
circulo = []
eliminados = 0

#Adicionando itens a lista
i = 0
while i < n:
    circulo.append(i + 1)
    i += 1

j = -1
while eliminados < len(circulo) - 1: #verifica número de eliminados

    #Elimina o número caso o número seja != de 0 e j == 1
    i = 0
    while i < len(circulo):
        if circulo[i] != 0:
            if j == 1:
                eliminados += 1
                if eliminados == x: # verifica se o número foi eliminado na posição x
                    print(f"Eliminado na posição {x}: {circulo[i]}")
                circulo[i] = 0
                j = j * (-1)
            else:
                j = j * (-1)
        i += 1

#Acha o ganhador e o imprime
i = 0
while i < len(circulo) -1:
    if circulo[i] != 0:
        print(f"Ganhadora: {circulo[i]}")
    i += 1
