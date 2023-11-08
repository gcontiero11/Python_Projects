import os

class Salas:
    deletado = 0
    numero = -1
    capacidade = -1 #100 ou 200

def isNumber(numero):
    if(str(numero).isnumeric()):
        return True
    else:
        return False
def abrirArquivo(nomeArquivo):
    salas = []
    if not os.path.exists(nomeArquivo):
        return salas
    arq = open(f"{nomeArquivo}" , 'r')
    for linha in arq:
        infos = linha.split(';')
        sala = Salas()
        sala.deletado = int(infos[0])
        sala.numero = int(infos[1])
        sala.capacidade = int(infos[2])

        salas.append(sala)
    arq.close()
    return salas

def sobrescreverArquivo(nomeArquivo , salas):
    arq = open(f"{nomeArquivo}",'w')
    for sala in salas:
        arq.write(str(sala.deletado) + ';' + str(sala.numero) + ';' + str(sala.capacidade) + "\n")
    arq.close

def inserirSala(salas):
    sala = Salas()
    sala.deletado = 0


    EhNumero = False
    while not EhNumero:
        sala.numero = input("Digite o Número da sala:")
        if not sala.numero.isnumeric():
            EhNumero = False
            print("\nNúmero Inválido!")
            print("Favor digitar um número inteiro\n")
        elif acharSala(salas,sala.numero) != -1:
            print("Numero Repetido")
        else:
            EhNumero = True


    EhNumero = False
    while not EhNumero:
        sala.capacidade = input("Digite a Capacidade (100 ou 200):")
        if not sala.capacidade.isnumeric():
            EhNumero = False
            print("\nNúmero Inválido!")
            print("Favor digitar um número inteiro\n")
        elif int(sala.capacidade) != 100 and int(sala.capacidade) != 200:
            EhNumero = False
            print("\nCapacidade Inválida!")
            print("Favor digitar um número dentre as opções\n")
        else:
            EhNumero = True
    salas.append(sala)
    return salas

def listarSalas(salas):
    i = 0
    for sala in salas:
        i += 1
        imprimirSala(sala,i)
    print("-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=--=-=-=-=-=-=-")

def imprimirSala(sala,i):
    if i > 0:        
        print("-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=--=-=-=-=-=-=-")
        print(f"Sala [{i}]\n")
        print(f"Número : {sala.numero}")
        print(f"Capacidade sala : {sala.capacidade}")
    else:
        print("-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=--=-=-=-=-=-=-")
        print("\n")
        print(f"Número : {sala.numero}")
        print(f"Capacidade sala : {sala.capacidade}")
        print("\n")

def acharSala(salas,num):
    i = 0
    for sala in salas:
        if sala.numero == int(num):
            return i
        i += 1
    return -1

def procurarSala(salas):
    EhNumero = False
    while not EhNumero:
        numero = input("Digite o Número da sala ou 0 caso queira voltar: ")
        if not numero.isnumeric():
            print("\nNúmero Inválido!")
            print("Favor digitar um número inteiro \n")
        else:
            EhNumero = True
    if numero == "0":
        print("Voltando")
    else:
        sala = acharSala(salas,int(numero))
        if sala == -1:
            print("\nSala não encontrada!")
            print("Verifique se o número da sala existe")
            print("Caso queira  sair basta digitar 0\n")
            procurarSala(salas)
        else:
            imprimirSala(sala,-1)

def alteraSala(salas):
    EhNumero = False
    while not EhNumero:
        numeroSala = input("Digite o numero da sala que deseja editar: ")
        indice = acharSala(salas,numeroSala)    
        if not isNumber(numeroSala):
            print("-=-=-=--=-=-=-=-=-=-=-=-")
            print("Favor digitar um numero!")
            print("-=-=-=--=-=-=-=-=-=-=-=-")
        elif indice == -1:
            print("-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=")
            print("Este numero de sala NÃO existe!")
            print("-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=")
        else:
            EhNumero = True
    opcao = -1
    while opcao != '0':
        opcao = menuAlteraSala()
        if opcao == '1':
            salas[indice].numero = alteraNumero(salas,salas[indice]) 
        elif opcao == '2':
            print(opcao) 
        elif opcao == '0':
            print("Voltando...")
        else:
            print("-=-=-=--=-=-=-=")
            print("Opção inválida!")
            print("-=-=-=--=-=-=-=")
    return salas
 
def menuAlteraSala():
    print("O que deseja mudar?")
    print("Numero.......[1]")
    print("Capacidade...[2]")
    print("Voltar......[0]")
    EhNumero = False
    while not EhNumero:
        opcao = input("------------->")
        if not isNumber(opcao):
            print("-=-=-=--=-=-=-=-=-=-=-=-")
            print("Favor digitar um numero!")
            print("-=-=-=--=-=-=-=-=-=-=-=-")
        else:
            EhNumero = True
    return opcao

def alteraNumero(salas,sala):
    EhNumero = False
    while not EhNumero:
        print(f"Numero antigo: {sala.numero}")
        sala.numero = input(f"Numero novo: ")
        if not isNumber(sala.numero):
            print("-=-=-=--=-=-=-=-=-=-=-=-")
            print("Favor digitar um numero!")
            print("-=-=-=--=-=-=-=-=-=-=-=-")
        elif acharSala(salas,sala.numero) != -1:
            print("-=-=-=--=-=-=-=-=-=-=-=-=-=-=-")
            print("Este numero de sala já existe!")
            print("-=-=-=--=-=-=-=-=-=-=-=-=-=-=-")
        else:
            EhNumero = True
    return sala.numero
def menu():
    EhNumero = False
    while not EhNumero:
        print("Escolha uma Opção")
        print("Inserir Sala........[1]")
        print("Listar Salas........[2]")
        print("Procurar uma Sala...[3]")
        print("Alterar uma Sala....[4]")
        print("Remover Sala........[5]")
        print("Sair................[0]")
        opcao = input("---------->")
        if not opcao.isnumeric():
            EhNumero = False
            print("\nOpção Inválida!")
            print("Favor digitar um número dentre as opções\n")
        else:
            EhNumero = True
    return opcao

def main():
    opcao = menu()
    nomeArquivo = "salas.txt"

    while opcao != '0':
        salas = abrirArquivo(nomeArquivo)

        #INSERIR
        if opcao == '1':
            print("\n")
            salas = inserirSala(salas)
            sobrescreverArquivo(nomeArquivo,salas)

        #LISTAR
        elif opcao == '2':
            print("\n")
            listarSalas(salas)

        #PROCURAR
        elif opcao == '3':
            print("\n")
            procurarSala(salas)

        #ALTERAR
        elif opcao == '4':
            print("\n")
            salas = alteraSala(salas)
            sobrescreverArquivo(nomeArquivo,salas)

        #REMOVER
        elif opcao == '5':
            print("\n")
            print(opcao)

        #SAIR
        elif opcao == '0':
            print("\n")
            print("SAINDO DO PROGRAMA...")

        #ERRO
        else:
            print("\nOpção Inválida!")
            print("Favor digitar um número dentre as opções\n")

        if opcao != '0':
            print("\n")
            opcao = menu()
